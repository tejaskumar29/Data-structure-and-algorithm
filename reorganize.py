"""
One-time script to reorganize existing LeetCode solutions into topic folders.
Run this from the root of your Data-structure-and-algorithm repo.

Usage:
    pip install requests
    python reorganize.py
"""

import os
import shutil
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


def get_problem_topics(slug: str) -> list[str]:
    """Fetch topic tags for a problem from LeetCode GraphQL API."""
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags {
                name
            }
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
        print(f"  [!] Could not fetch topics for '{slug}': {e}")
        return []


def pick_folder(topics: list[str]) -> str:
    """Pick the best topic folder based on priority order."""
    for priority_topic in TOPIC_PRIORITY:
        if priority_topic in topics:
            return TOPIC_FOLDER_MAP.get(priority_topic, "Misc")
    return "Misc"


def extract_slug(folder_name: str) -> str:
    """Extract the problem slug from folder name like '0238-product-of-array-except-self'."""
    # Remove leading number prefix
    parts = folder_name.split("-", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return parts[1]
    return folder_name


def main():
    cwd = os.getcwd()
    print(f"Running in: {cwd}\n")

    # Find all problem folders (start with a number)
    problem_folders = [
        d for d in os.listdir(cwd)
        if os.path.isdir(d) and d[0].isdigit()
    ]

    if not problem_folders:
        print("No problem folders found at root. Make sure you're in the repo root.")
        return

    print(f"Found {len(problem_folders)} problem(s) to reorganize:\n")

    for folder in sorted(problem_folders):
        slug = extract_slug(folder)
        print(f"Processing: {folder}")
        print(f"  Slug: {slug}")

        topics = get_problem_topics(slug)
        print(f"  Topics: {topics if topics else 'None found'}")

        target_category = pick_folder(topics)
        print(f"  -> Moving to: {target_category}/")

        target_dir = os.path.join(cwd, target_category)
        os.makedirs(target_dir, exist_ok=True)

        src = os.path.join(cwd, folder)
        dst = os.path.join(target_dir, folder)

        if os.path.exists(dst):
            print(f"  [!] Already exists at destination, skipping.")
        else:
            shutil.move(src, dst)
            print(f"  Done.")

        time.sleep(0.5)  # Be polite to LeetCode API
        print()

    print("Reorganization complete!")
    print("\nNext steps:")
    print("  git add .")
    print('  git commit -m "Reorganize solutions into topic folders"')
    print("  git push")


if __name__ == "__main__":
    main()
