import tkinter as tk
from PIL import Image,ImageTk
import os
import csv
import argparse


class ImageClassifyer(tk.Frame):


    def __init__(self, parent, foldername, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        self.root.wm_title("Classify Image")   
        src = "./{}/".format(foldername)

        self.list_images = []
        for d in os.listdir(src):
            self.list_images.append(d)

        self.frame1 = tk.Frame(self.root, width=800, height=1200, bd=2)
        self.frame1.grid(row=1, column=0)
        # self.frame2 = tk.Frame(self.root, width=500, height=400, bd=1)
        # self.frame2.grid(row=1, column=1)

        self.cv1 = tk.Canvas(self.frame1, height=700, width=1100, background="white", bd=1, relief=tk.RAISED)
        self.cv1.grid(row=1,column=0)
        # self.cv2 = tk.Canvas(self.frame2, height=390, width=490, bd=2, relief=tk.SUNKEN)
        # self.cv2.grid(row=1,column=0)

        claButton = tk.Button(self.root, text='Accept', height=2, width=10, command=self.classify_obj)
        claButton.grid(row=0, column=1, padx=2, pady=2)
        broButton = tk.Button(self.root, text='Next', height=2, width=8, command = self.next_image)
        broButton.grid(row=0, column=0, padx=2, pady=2)

        self.counter = 0
        self.max_count = len(self.list_images)-1
        self.next_image()

    def classify_obj(self):
        f_name = self.list_images[self.counter]
        print(f_name)
        with open('accepted_file.csv', 'a') as myfile:
            wr = csv.writer(myfile)
            wr.writerow([f_name])

    def next_image(self):

        if self.counter > self.max_count:
            print("No more images")
        else:
            im = Image.open("{}{}".format("./{}/".format(foldername), self.list_images[self.counter]))
            if (1100-im.size[0])<(700-im.size[1]):
                width = 1100
                height = width*im.size[1]/im.size[0]
                self.next_step(height, width)
            else:
                height = 700
                width = height*im.size[0]/im.size[1]
                self.next_step(height, width)

    def next_step(self, height, width):
        self.im = Image.open("{}{}".format("./{}/".format(foldername), self.list_images[self.counter]))
        self.im.thumbnail((width, height), Image.ANTIALIAS)
        self.root.photo = ImageTk.PhotoImage(self.im)
        self.photo = ImageTk.PhotoImage(self.im)

        if self.counter == 0:
            self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)

        else:
            self.im.thumbnail((width, height), Image.ANTIALIAS)
            self.cv1.delete("all")
            self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
        self.counter += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foldername", "-f", help="open the specified video (overrides the --camera_id option)",
                        type=str, default=None)
    args = parser.parse_args()
    foldername = args.foldername

    root = tk.Tk() 
    MyApp = ImageClassifyer(root, foldername=foldername)
    tk.mainloop()