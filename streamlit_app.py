import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim

class Model(nn.Module):
  def __init__(self):
    super(Model,self).__init__()
    self.w = nn.Parameter(torch.randn(1,dtype=torch.float32,requires_grad=True))
    self.b = nn.Parameter(torch.randn(1,dtype=torch.float32,requires_grad=True))
  def forward(self,x):
    return self.w*x + self.b

model = Model()

x = torch.tensor(float(input("今日の気温を教えてください"))).unsqueeze(dim=2)
y = model(x)

st.write(f"今日の売り上げは{y}です")
