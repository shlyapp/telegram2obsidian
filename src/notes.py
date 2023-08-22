from datetime import datetime

from git import Repo

from config import PATH_TO_REPO


repo = Repo(PATH_TO_REPO)


def add_new_note(note_text: str):
    current_datetime = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    file_name = f"telegram-message_{current_datetime}.md"
    with open(f"{PATH_TO_REPO}/{file_name}", "w") as file:
        file.write(note_text)
    repo.index.add([file_name])
    commit_message = f"Telegram message - {current_datetime}"
    repo.index.commit(commit_message)
    repo.remotes.origin.push()
