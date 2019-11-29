# PyGame Breakout

This is a simple implementation with Python 3 and PyGame of the classic [Breakout](https://en.wikipedia.org/wiki/Breakout_(video_game)) game. The purpose is to serve as a demo game for a
series of articles on building games with Python 3 and PyGame:

- [Building Games With Python 3 and Pygame: Part 1](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-1--cms-30081)
- [Building Games With Python 3 and Pygame: Part 2](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-2--cms-30082)
- [Building Games With Python 3 and Pygame: Part 3](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-3--cms-30083)
- [Building Games With Python 3 and Pygame: Part 4](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-4--cms-30084)
- [Building Games With Python 3 and Pygame: Part 5](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-5--cms-30085)

# Features

- Simple generic GameObject and TextObject
- Simple generic Game object
- Simple generic button
- Config file
- Handling keyboard and mouse events
- Bricks, paddle and ball
- Managing paddle movement
- Handling collisions of the ball with everything
- Background image
- Sound effects
- Extensible special effects system

# Installation and usage

You need [Python 3.8](https://docs.python.org/3.8/) and [Pipenv]() installed. Then clone the [repository](https://gitlab.com/the-gigi/pygame-breakout) and type:

```
pipenv install
```

You should see something like:

```
$ pipenv install
Creating a virtualenv for this project…
Pipfile: /Users/gigi.sayfan/git/pygame-breakout/Pipfile
Using /usr/local/bin/python3 (3.7.5) to create virtualenv…
⠋ Creating virtual environment...Using base prefix '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/gigi.sayfan/.local/share/virtualenvs/pygame-breakout-mgkKDQCD/bin/python3.7
Also creating executable in /Users/gigi.sayfan/.local/share/virtualenvs/pygame-breakout-mgkKDQCD/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/local/bin/python3

✔ Successfully created virtual environment!
Virtualenv location: /Users/gigi.sayfan/.local/share/virtualenvs/pygame-breakout-mgkKDQCD
Pipfile.lock (217131) out of date, updating to (0d3bd9)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (217131)!
Installing dependencies from Pipfile.lock (217131)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:07
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

To run the game type:

```
pipenv run python game.py
```

# Credits

I used some color constants I found in this nice article: https://www.webucator.com/blog/2015/03/python-color-constants-module/
