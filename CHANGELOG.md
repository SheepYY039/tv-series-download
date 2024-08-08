## v1.4.1 (2024-08-08)

### Fix

- :bug: new release bug fixes

## v1.4.0 (2024-08-08)

### Feat

- **CLI**: :children_crossing: Added `--dry-run` flag
- **searchbar**: add searchbar to webui
- **django**: settings form
- **settings**: add sources checkbox
- **django**: setup basic web structure
- **django**: init django

### Fix

- **Source**: :bug: fix xiaobao source download link not found bug
- **bulma**: fix bulma css extensions

## v1.3.4 (2024-02-16)

### Fix

- fix config file backwards compatibility

## v1.3.3 (2024-02-15)

### Perf

- change config to use dynaconf

## v1.3.2 (2023-11-09)

### Fix

- File Exists function checks non-existent directory

### Refactor

- Clean up episode.py

## v1.3.1 (2023-10-23)

### Fix

- Get episode number from existing episode for calculation
- create Season Directory before checking local files

### Refactor

- remove unused variable

### Perf

- remove unused init command

## v1.3.0 (2023-10-22)

### Feat

- improve ep exist detection and set ep no.

### Fix

- ssstv.py scrape error fix

### Refactor

- Clean code and fix types
- Clean code for download.py file
- clean code after poetry migration

### Perf

- add poetry script to shorten run command
- print message "name" already exists not "filename"
- reduce code complexity for sources iteration

## v1.2.1 (2023-09-02)

### Feat

- **download**: flag to download specials only

### Fix

- _variables were created as const, didn't update according to config state

## v1.2.0 (2023-07-31)

### Feat

- **cli**: New cmd to clean empty directories
- **flag**: Allow specifying base path in cli
- **cli**: Added new CLI feature to print current State
- **cli**: Added new CLI function to remove show
- new command to list all existing shows
- convert all folder names to simplified

### Fix

- **cli**: consider case when show does not have year

### Refactor

- Separate instance state and user config

### Perf

- apply config before setting local state

## v1.1.3 (2023-07-24)

### Fix

- Typing syntax error

## v1.1.2 (2023-07-24)

### Fix

- catch error during download and aport
- return None if error exists and ignore result

## v1.1.1 (2023-07-24)

### Fix

- 777TV year matching regex fix

### Perf

- catch exception upon connection error

## v1.1.0 (2023-07-24)

### Feat

- set source simplified or traditional search_query for automatic translation
- create general series directory if not exist in base
- **config**: created basic config setup

### Refactor

- Cleanup code

## v1.0.1 (2023-07-12)

### Refactor

- added all sources import in __init__.py and generalized ssstv urls into source_url and relative path

## v1.0.0 (2023-07-11)

### Feat

- **source**: Added new media source 777tv

### Fix

- websockets auto patch failed due to pyppeteer==1.0.2 dependencies

## v1.0.0a0 (2023-07-11)

### Fix

- update COMMIT_MSG_HOOK in makefile
