"""
.github/scripts/sort_solution.py

Called by the GitHub Action after each push.
Detects new problem folders at the repo root and moves them into topic folders.
"""

import os
import shutil
import subprocess
import requests
import time

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

TOPIC_PRIORITY = [
    "Array", "String", "Hash Table", "Dynamic Programming",
    "Math", "Sorting", "Greedy", "Depth-First Search",
    "Binary Search", "Breadth-First Search", "Tree", "Matrix",
    "Two Pointers", "Bit Manipulation", "Binary Tree", "Heap (Priority Queue)",
    "Graph", "Sliding Window", "Backtracking", "Linked List",
    "Stack", "Queue", "Recursion", "Divide and Conquer",
    "Trie", "Monotonic Stack", "Union Find",
]

TOPIC_FOLDER_MAP = {
    "Array": "Arrays",
    "String": "Strings",
    "Hash Table": "Hash-Table",
    "Dynamic Programming": "Dynamic-Programming",
    "Math": "Math",
    "Sorting": "Sorting",
    "Greedy": "Greedy",
    "Depth-First Search": "Graphs",
    "Binary Search": "Binary-Search",
    "Breadth-First Search": "Graphs",
    "Tree": "Trees",
    "Matrix": "Arrays",
    "Two Pointers": "Two-Pointers",
    "Bit Manipulation": "Bit-Manipulation",
    "Binary Tree": "Trees",
    "Heap (Priority Queue)": "Heap",
    "Graph": "Graphs",
    "Sliding Window": "Sliding-Window",
    "Backtracking": "Backtracking",
    "Linked List": "Linked-List",
    "Stack": "Stack",
    "Queue": "Queue",
    "Recursion": "Recursion",
    "Divide and Conquer": "Divide-and-Conquer",
    "Trie": "Trie",
    "Monotonic Stack": "Stack",
    "Union Find": "Graphs",
}

# Folders to ignore (not problem folders)
IGNORE_FOLDERS = {".git", ".github", "Arrays", "Strings", "Hash-Table",
                  "Dynamic-Programming", "Math", "Sorting", "Greedy", "Graphs",
                  "Binary-Search", "Trees", "Two-Pointers", "Bit-Manipulation",
                  "Heap", "Sliding-Window", "Backtracking", "Linked-List",
                  "Stack", "Queue", "Recursion", "Divide-and-Conquer", "Trie", "Misc"}


def get_new_folders() -> list[str]:
    """Get folders added in the latest commit at the repo root."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=A", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    changed = result.stdout.strip().splitlines()
    # Find folders at root level (depth = 1 path component before /)
    new_folders = set()
    for path in changed:
        parts = path.split("/")
        if len(parts) >= 1:
            folder = parts[0]
            if folder[0].isdigit() and folder not in IGNORE_FOLDERS:
                new_folders.add(folder)
    return list(new_folders)


def get_problem_topics(slug: str) -> list[str]:
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags { name }
        }
    }
    """
    try:
        response = requests.post(
            LEETCODE_GRAPHQL,
            json={"query": query, "variables": {"titleSlug": slug}},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        data = response.json()
        tags = data["data"]["question"]["topicTags"]
        return [tag["name"] for tag in tags]
    except Exception as e:
        print(f"[!] Could not fetch topics for '{slug}': {e}")
        return []


def pick_folder(topics: list[str]) -> str:
    for priority_topic in TOPIC_PRIORITY:
        if priority_topic in topics:
            return TOPIC_FOLDER_MAP.get(priority_topic, "Misc")
    return "Misc"


def extract_slug(folder_name: str) -> str:
    parts = folder_name.split("-", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return parts[1]
    return folder_name


def main():
    cwd = os.getcwd()
    new_folders = get_new_folders()

    if not new_folders:
        print("No new problem folders detected at root. Nothing to sort.")
        return

    for folder in new_folders:
        src = os.path.join(cwd, folder)
        if not os.path.isdir(src):
            continue

        slug = extract_slug(folder)
        print(f"New problem: {folder} (slug: {slug})")

        topics = get_problem_topics(slug)
        print(f"  Topics: {topics}")

        target_category = pick_folder(topics)
        print(f"  -> Target folder: {target_category}/")

        target_dir = os.path.join(cwd, target_category)
        os.makedirs(target_dir, exist_ok=True)

        dst = os.path.join(target_dir, folder)
        if os.path.exists(dst):
            print(f"  [!] Already exists at destination, skipping.")
        else:
            shutil.move(src, dst)
            print(f"  Moved successfully.")

        time.sleep(0.5)


if __name__ == "__main__":
    main()
