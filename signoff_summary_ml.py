# signoff_summary_ml.py
# Summary dashboard for RTL-to-GDS signoff flow with CLI, optional plotting, and ML prediction

import os
import re
import argparse
import matplotlib.pyplot as plt
from terminal_utils import color_text

# Simulated function: parse a dummy PrimeTime timing report
def parse_timing_report(file_path):
    """Extract worst slack and total violations from a timing report."""
    worst_slack = None
    violations = 0

    with open(file_path, 'r') as f:
        for line in f:
            if 'slack (VIOLATED)' in line:
                match = re.search(r'slack \(VIOLATED\)\s*:\s*(-?\d+\.\d+)', line)
                if match:
                    slack = float(match.group(1))
                    if worst_slack is None or slack < worst_slack:
                        worst_slack = slack
                    violations += 1
    return worst_slack, violations

# Simulated function: parse an area report
def parse_area_report(file_path):
    """Extract total cell area from area report."""
    with open(file_path, 'r') as f:
        for line in f:
            if 'Total cell area:' in line:
                match = re.search(r'Total cell area:\s*(\d+\.\d+)', line)
                if match:
                    return float(match.group(1))
    return 0.0


# Entry point
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Signoff Flow Tracker: summarize timing and area reports.'
    )
    parser.add_argument(
        '--timing', required=True,
        help='Path to PrimeTime timing report (e.g., pt_report.txt)'
    )
    parser.add_argument(
        '--area', required=True,
        help='Path to synthesis area report (e.g., area_report.txt)'
    )
    parser.add_argument(
        '--plot', action='store_true',
        help='Enable plotting bar chart of signoff metrics'
    )
    parser.add_argument(
        '--out', type=str,
        help='Optional: save summary to a text file (e.g., summary.txt)'
    )
    parser.add_argument(
        '--ml', type=str,
        help='Optional: path to pre-trained ML model (e.g., model.pkl) to predict block status'
    )

    args = parser.parse_args()

    slack, num_violations = parse_timing_report(args.timing)
    area = parse_area_report(args.area)

    summary = (
        f"--- Signoff Summary ---\n"
        f"Worst Slack: {slack} ns\n"
        f"Violations: {num_violations}\n"
        f"Total Cell Area: {area} sq units\n"
    )

    print(summary)

# Cheking Argumens
    if args.out:
        with open(args.out, 'w') as f:
            f.write(summary)
        print(f"Summary saved to {args.out}")

    if args.ml:
        try:
            from joblib import load
            model = load(args.ml)
            prediction = model.predict([[slack, num_violations, area]])[0]
            colored_prediction = color_text(prediction, prediction)
            print(f"ML Predicted Status: {colored_prediction}")
        except Exception as e:
            print(f"ML Prediction failed: {e}")

    if args.plot:
        labels = ['Worst Slack (ns)', 'Violations', 'Total Area (k)']
        values = [slack, num_violations, area / 1000]  # scale area
        plt.bar(labels, values, color=['red', 'orange', 'green'])
        for i, v in enumerate(values):
            plt.text(i, v + 0.05 * max(values), f"{v:.2f}", ha='center', va='bottom')
        plt.title('Signoff Report Summary')
        plt.ylabel('Metric')
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.show()
