import requests
import time
import tqdm

def re_run_all_jobs(workflow_run_url, api_token):
    
    # Extract the run ID from the URL
    run_id = workflow_run_url.split('/')[-1]

    # Construct the API endpoint URL
    api_url = f"https://api.github.com/repos/{workflow_run_url.split('/')[3]}/{workflow_run_url.split('/')[4]}/actions/runs/{run_id}/rerun"

    # Prepare the headers with the provided API token
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Mozilla/5.0"
    }

    # Send a POST request to the API endpoint to trigger re-run
    try:
        response = requests.post(api_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    if response.status_code == 201:
        print("Re-run successfully triggered!")
    else:
        print(f"Failed to trigger re-run. Status code: {response.status_code}")

print("Wating to wakeup runner...")

# Delay function execution for 5 hours and 55 minutes (15000 seconds)
#time.sleep(5 * 60 * 60 + 55 * 60)
for i in tqdm.tqdm(range(10)):
    time.sleep(1)

# Example usage

workflow_run_url = "https://github.com/dayanid/wakeuprunner/actions/runs/5276625801"
api_token = "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"
re_run_all_jobs(workflow_run_url, api_token)
