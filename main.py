import tkinter as tk
import decimal
import pygame
import random
pygame.init()
sarki = [pygame.mixer.Sound("gece872.mp3"), pygame.mixer.Sound("ruzgar872.mp3"), pygame.mixer.Sound("yagmur872.mp3")]
def sarkii():
  pygame.mixer.stop()
  rndm = random.randint(0, 2)
  sarki[rndm].play(-1)
  arkaplan = tk.Canvas(p, highlightthickness=0)
  arkaplan.pack(fill="both", expand=True)
  arkaplan.delete("all")
  if rndm == 0:
    arkaplan = tk.Canvas(p, bg="#0043ED", highlightthickness=0)
    arkaplan.pack(fill="both", expand=True)
    arkaplan.create_oval(25, 25, 150, 150, fill="yellow", outline="")
  elif rndm == 1:
    arkaplan = tk.Canvas(p, bg="#87EDFF", highlightthickness=0)
    arkaplan.pack(fill="both", expand=True)
    arkaplan.create_oval(25, 25, 150, 150, fill="white", outline="")
  else:
    arkaplan = tk.Canvas(p, bg="#4C9492", highlightthickness=0)
    arkaplan.pack(fill="both", expand=True)
    arkaplan.create_oval(25, 25, 150, 150, fill="gray", outline="")
  p.after(60000, sarkii)
p = tk.Tk()
sanse = random.randint(0, 2)
p.geometry("720x480")

p.after(0, sarkii)
p.mainloop()