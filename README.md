
# Prologue

A simple open source web based video editor using ffmpeg which will run on localhost



## API Reference

#### Get all items

```
  cut
```
will trim a video down with the provided inputs
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `_from` | `integer` | **Required**. from where do you want to trim your video |
| `_to` | `integer` | **Required**. till where do you want to trim your video |

#### Get item

```
  scale
```
scale up or down a video to a given width and height

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `width`      | `integer` | **Required**. width of the new scale |
| `height`      | `integer` | **Default: -1**. height of the new scale `-1` denotes that it will scale the height accordingly to mantain the aspect ratio |



## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Authors

- [@ohayouarmaan](https://www.github.com/ohayouarmaan)

