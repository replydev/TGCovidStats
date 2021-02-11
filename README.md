# 🦠 TG Covid-19 Stats

## Overview
I think that one way to fight Covid-19 is to spread information to the population.

[Covid-19 Stats](https://github.com/replydev/Covid-Stats) it's an easy deployable Telegram Bot that fetch italy Covid-19 statistics
and dynamically organizes them in a graph, to look at the trend of the epidemic over time.

## Which data Covid-19 Stats uses?
This bot uses ONLY official data pushed by the official [Github Account of the Italian Civil Protection](https://github.com/pcm-dpc/COVID-19).

## How to deploy
- Install the `python3` package in your system.
- Install the `mariadb-server` DBMS.
- Log in your MariaDB server and create a new database and a new user.
- Create a new Telegram Bot using [BotFather](https://t.me/BotFather).
- After creating your new bot please note your **API Token** and your **bot username**.
- Run these commands:
```
git clone https://github.com/replydev/TGCovidStats.git
cd TGCovidStats
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m TgCovidStats
```
- The first run will fail, but the program will create an example config file called `config.json`.
- Open the config file, and insert the required attributes.
- Edit the `update_time` attribute inserting the specific hour of the day when you want the bot to update his dataset. I advice `18:00` or `18:30`. 
- Restart the bot using `python -m TgCovidStats` and enjoy 🎉.

## Contribution
This probably is the first project that I made for others and not only for me, so this gives another meaning to the word **contribution**.

I want this to become a community project so any contribution, as always, is welcome!
Just make a pull request and if your code meet my (low) code standards I will be happy to merge your **contribution**.

### Stay Home, Stay Safe 😷
