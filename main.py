# OSRS Highscores GIM Prestige Scraper
# Nick Lueth
# Last edited: 4/18/2025

import requests
from bs4 import BeautifulSoup

your_team = "".lower()  # Your team name
your_group_size = ""  # Integer size of your group


# Function to scrape a single page and extract team names
def scrape_page(page_num):
    url = f"https://secure.runescape.com/m=hiscore_oldschool_ironman/group-ironman/?groupSize={your_group_size}&page={page_num}"
    response = requests.get(url)
    response.raise_for_status()  # Will raise an error if the request failed

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <tr> elements that contain the Group Prestiged image with title="Group Prestiged"
    prestiged_teams = soup.find_all('tr', class_='uc-scroll__table-row')

    # List to store the team names from this page
    teams = []

    # Iterate through all teams on this page
    for team in prestiged_teams:
        prestige_icon = team.find('img', title="Group Prestiged")

        if prestige_icon:
            # Extract the team name from the <a> tag
            team_name_tag = team.find('a', class_='uc-scroll__link')
            if team_name_tag:
                team_name = team_name_tag.get_text(strip=True)
                teams.append(team_name)

    return teams


# Main function to loop through the pages and search for your team
def main():
    page_num = 1
    leaderboard = []

    # Keep scraping pages until we find your team
    while True:
        print(f"Scraping page {page_num}...")

        # Get the list of teams from the current page
        teams = scrape_page(page_num)

        # Check if any team is your_team
        for team_name in teams:
            leaderboard.append(team_name)
            if team_name.lower() == your_team:
                print(f"Found {your_team}! Stopping the scrape.")
                return leaderboard

        # If your team wasn't found, move to the next page
        page_num += 1


# Function to remove all duplicates from the leaderboard while preserving the order
def remove_duplicates(leaderboard):
    seen = set()  # To track already encountered team names
    unique_teams = []

    # Iterate through the leaderboard and add only unseen teams
    for team_name in leaderboard:
        if team_name.lower() not in seen:  # We use .lower() to ensure case-insensitive matching
            unique_teams.append(team_name)
            seen.add(team_name.lower())  # Track the team as seen

    return unique_teams


# Call the main function and output the leaderboard
leaderboard = main()

# Remove any duplicates from the leaderboard
final_leaderboard = remove_duplicates(leaderboard)

# Print the final leaderboard in ordered format
print("\nFinal Leaderboard:")
for i, team_name in enumerate(final_leaderboard, start=1):
    print(f"{i}. {team_name}")
