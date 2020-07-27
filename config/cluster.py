"""Configuration for job submission to a cluster.
"""
import os

# Command to use when submitting to cluster.
SUBMIT_COMMAND = os.environ.get("DASHBOARD_QSUBMIT_CMD") or "sbatch"

# Options to always set during submission (e.g. QOS)
SUBMIT_OPTIONS = os.environ.get("DASHBOARD_QSUBMIT_OPTIONS") or ""

# Job script location. If changed from dashboard/queue_jobs, the folder
# must contain scripts matching the names of those in the original folder.
SUBMIT_SCRIPTS = (
    os.environ.get("DASHBOARD_QSUBMIT_SCRIPTS") or
    os.path.join(
        os.path.dirname(os.path.realpath(__name__)),
        '..dashboard/queue_jobs'
        )
    )
