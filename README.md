# OSRS Highscores GIM Prestige Scraper
Created by: Nick Lueth\n
Last Edited: 4/18/2025

This Python script scrapes the leaderboard of "Group Prestiged" Ironman teams from the [Old School RuneScape Ironman Group Leaderboard](https://secure.runescape.com/m=hiscore_oldschool_ironman/group-ironman/) and generates a numbered leaderboard of the teams until it finds the specified team name. The script removes any duplicate teams from the final leaderboard and prints it in sequential order.

## Features
- Scrapes multiple pages of the leaderboard.
- Collects teams that are marked as "Group Prestiged".
- Stops once it finds the specified team.
- Removes duplicate teams from the final leaderboard.
- Prints a numbered leaderboard in the order the teams were parsed.

## Prerequisites

Before you run the script, make sure you have Python 3 installed. Additionally, you'll need to install the required libraries:

- `requests`: to send HTTP requests and fetch the webpage.
- `beautifulsoup4`: to parse and extract data from the HTML.

### Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script file.
2. Edit the "your_team" and "your_group_size" variables within the main python file.
3. Run the script:

```bash
python3 main.py
```

3. The script will scrape the pages starting from page 1, collecting all the "Group Prestiged" teams.
4. It will stop once it finds the specified team and print the final leaderboard with no duplicates.

### Example Output:

```
Scraping page 1...
Scraping page 2...
...
Found 'myawesometeam'! Stopping the scrape.

Final Leaderboard:
1. TeamA
2. TeamB
3. TeamC
...
25. myawesometeam
```

### Notes:
- The script will continue scraping until it finds your team or runs into an error.
- If a team name appears multiple times across pages, only the first occurrence will appear in the final leaderboard.
- The script is case-insensitive when checking for duplicate team names.

## Contributing

Feel free to open issues or pull requests if you'd like to contribute improvements or bug fixes.
