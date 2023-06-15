from github import Github

def re_run_workflow_run(workflow_run_url, app_installation_token):
    # Extract the run ID from the URL
    run_id = workflow_run_url.split('/')[-1]

    # Create a PyGithub instance using the installation token
    g = Github(base_url="https://api.github.com", login_or_token=app_installation_token)

    # Get the repository and workflow run objects
    repo = g.get_repo("dayanid/wakeuprunner")
    run = repo.get_workflow_run(int(run_id))

    # Trigger re-run of the workflow run
    re_run = run.rerun()

    if re_run:
        print("Re-run successfully triggered!")
    else:
        print("Failed to trigger re-run.")

# Example usage
workflow_run_url = "https://github.com/dayanid/wakeuprunner/actions/runs/5276625801"
app_installation_token = "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"
re_run_workflow_run(workflow_run_url, app_installation_token)
