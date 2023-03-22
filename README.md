
# Prologue

A simple open source web based video editor using ffmpeg which will run on localhost



## API Reference

### Trim a video

```
  cut
```
will trim a video down with the provided inputs
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `_from` | `integer` | **Required**. from where do you want to trim your video |
| `_to` | `integer` | **Required**. till where do you want to trim your video |


### Scale to a specific resolution

```
  scale
```
scale up or down a video to a given width and height

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `width`      | `integer` | **Required**. width of the new scale |
| `height`      | `integer` | **Default: -1**. height of the new scale `-1` denotes that it will scale the height accordingly to mantain the aspect ratio |


### Manipulate volume

```
  volume
```
change audio of a given stream

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `volume`      | `float 0 <= x <= 1` | **Required**. Manipulates the volume of the audio stream |


## Current Plan

1. [  ] I'll be working on rendering a piece of html as a transparent jpg and then it can be used to add stickers or whatever you want to

2. [  ] Create a community / write blog posts about prologue it'll help in involving more people into this project and thus accelerating the development of prologue

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Authors

- [@ohayouarmaan](https://www.github.com/ohayouarmaan)

