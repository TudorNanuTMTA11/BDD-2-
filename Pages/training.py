import logging

from base_page import Base_page

class Training(Base_page): #am construit o clasa
    def training_image(self):
        try:
            training_image = self.chrome.find_element(*self.TRAINING_IMAGE)
            if training_image:
                training_image.click()
            else:
                raise AssertionError('Training image element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the training image: {str(i)}")

    def training_option(self):
        try:
            training_option = self.chrome.find_element(*self.TRAINING_OPTION)
            if training_option:
                training_option.click()
            else:
                raise AssertionError('Training option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the training option: {str(i)}")

    def video_download(self):
        try:
            video_download = self.chrome.find_element(*self.MESSAGE_INFO)
            if video_download:
                video_download.is_displayed()
            else:
                raise AssertionError('Message info element was not displayed')
        except Exception as i:
            logging.error(f"An error occurred while displaying the message info: {str(i)}")

    def video_download_option(self):
        try:
            video_download_option = self.chrome.find_element(*self.VIDEO_DOWNLOAD_OPTION)
            if video_download_option:
                video_download_option.click()
            else:
                raise AssertionError('Video download option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the video download option: {str(i)}")







