# Webcam Image Filtering and Segmentation Project

## Overview

This project uses OpenCV and the `cvzone.SelfiSegmentationModule` to apply various filters and effects to webcam video frames in real-time. The program allows the user to select different parts of the image (the person, background, or the whole frame) and apply effects such as sepia, emboss, edge enhancement, pixelation, brightness adjustment, and Gaussian blur. The filtered image can also be saved to the user's desktop.

## Features

1. **Real-Time Webcam Capture**: 
   - The program captures video feed from the user's webcam, and allows them to apply various filters and effects.

2. **Segmentation and Filtering**:
   - **Person Segmentation**: Using the `cvzone.SelfiSegmentationModule`, the program can detect and segment the person from the background.
   - **Filter Application**: Users can apply the following filters to either the person, the background, or the entire frame:
     - Gaussian Blur
     - Sepia Effect
     - Pixelation
     - Emboss Effect
     - Edge Enhancement
     - Brightness Control (Increase/Decrease)

3. **Image Saving**:
   - The filtered image can be saved to the desktop with a timestamp-based unique filename.

## How It Works

1. **Selection of Application Area**:
   - On startup, the user is prompted to select whether the filter should be applied to the person (`1`), the background (`2`), or the entire frame (`3`).

2. **Filter Selection**:
   - During the video feed, users can choose the desired filter by pressing the corresponding key:
     - `1`: Gaussian Blur
     - `2`: Sepia Filter
     - `3`: Pixelation
     - `4`: Emboss Effect
     - `5`: Edge Enhancement
     - `i`: Increase Brightness
     - `d`: Decrease Brightness

3. **Save Image**:
   - Press `s` to save the current frame to the desktop in a folder named `project` with a unique filename.

4. **Quit**:
   - Press `c` to exit the program.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- cvzone (`cvzone`)

You can install the required dependencies with the following command:

```bash
pip install opencv-python numpy cvzone
```

## Running the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd your-repo-name
   ```

3. **Run the script**:
   ```bash
   python your_script_name.py
   ```

## Example Usage

- Upon running the program, you will be prompted to select which part of the frame you want to apply the filters to:
  - Press `1` for the person, `2` for the background, or `3` for the whole frame.
- Once you’ve made your selection, you can apply various filters in real-time by pressing the corresponding key.
- Press `s` to save the filtered frame to your desktop.

## Project Structure

- `your_script_name.py`: The main Python script containing the webcam capture, segmentation, and filter application logic.

## Future Enhancements

- **Additional Filters**: Adding more advanced filters and effects.
- **Customization**: Allowing users to adjust filter parameters dynamically.
- **GUI Implementation**: Creating a graphical user interface (GUI) for easier interaction and filter selection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Feel free to fork this project and contribute by submitting pull requests. Any improvements or new features are welcome!

---

Enjoy filtering your webcam images and experimenting with effects in real-time!

## Author

[Your Name](https://github.com/yourusername)

