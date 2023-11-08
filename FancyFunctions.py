# extra functions

#"""
def custom_progress_bar(current_step, total_steps):
	percent_complete = (current_step / total_steps) * 100
	progress = "[" + "#" * int(percent_complete) + "-" * (100 - int(percent_complete)) + "]"
	progress_text = f"{int(percent_complete)}% Complete ({current_step}/{total_steps})"
	print(f"\r{progress_text} {progress}", end="") # Use carriage return to overwrite the previous progress
	if current_step == total_steps: # When all steps are completed, print a newline to move to the next line
		print("", flush=True)
#"""

