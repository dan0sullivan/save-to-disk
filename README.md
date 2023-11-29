# save-to-disk

## Instructions
### Download save-to-disk
```
go install github.com/pion/webrtc/v4/examples/save-to-disk@latest
```

### Open save-to-disk example page
[jsfiddle.net](https://jsfiddle.net/s179hacu/) you should see your Webcam, two text-areas and two buttons: `Copy browser SDP to clipboard`, `Start Session`.

### Run save-to-disk, with your browsers SessionDescription as stdin
In the jsfiddle the top textarea is your browser's Session Description. Press `Copy browser SDP to clipboard` or copy the base64 string manually.
We will use this value in the next step.

#### Linux/macOS
Run `echo $BROWSER_SDP | save-to-disk`
#### Windows
1. Paste the SessionDescription into a file.
1. Run `save-to-disk < my_file`

### Input save-to-disk's SessionDescription into your browser
Copy the text that `save-to-disk` just emitted and copy into second text area

### Hit 'Start Session' in jsfiddle, wait, close jsfiddle, enjoy your video!
In the folder you ran `save-to-disk` you should now have a file `output-1.ivf` play with your video player of choice!
> Note: In order to correctly create the files, the remote client (JSFiddle) should be closed. The Go example will automatically close itself.

### Run jpegs.py
this will convert the output.ivf file (remember to terminate the webrtc code by pressing ctrl C) into jpeg images, the yolo object detection then runs object detection on these images.

