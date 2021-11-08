import streamlit as st

import pandas as pd

import re

import csv

import random

import os

st.title("ポケモンの名前でしりとり")

with open('pokemon_status.csv',encoding='shift-jis') as file:
    pokemon=[]
    for row in file:
        name=row.rstrip()
        pokemon.append(name)
              

def is_katakana(str):
    katakana=re.compile('[ァ-ヶー・]+')
    if katakana.fullmatch(str):
        pass
    else:
        st.write('カタカナで入力してね')
        return False

def is_brank(str):
    if len(str)==0:
        st.write('入力してね')
        return False

def is_pokemon(str):
    if str in pokemon == False:
        st.write('ポケモンの名前を入力してね')
        return False

def is_end(str):
    if str.endswith('ン')==True:
        return False
    else:
        return True

skip1='ァィゥェォッャュョー'

poke=st.text_input(label='ポケモンの名前を入力してね')

count=1
while True:
    

    if is_brank(poke)==False:
        break
    if is_katakana(poke)==False:
        break
    if is_pokemon(poke)==False:
        break

    pokemon.remove(poke)

    choice=[]
    choice_n=[]
    for poke_name in pokemon:
        for i in skip1:
            if poke.endswith(i)==True:
                if poke[-2]==i:
                    if (poke_name.startswith(poke[-3])==True):
                        choice.append(poke_name)

                elif (poke_name.startswith(poke[-2])==True):
                    choice.append(poke_name)
                      
        
            if poke_name.startswith(poke[-1]) and (is_end(poke_name)==True):
                choice.append(poke_name)

    for poke_name in choice:
        if is_end(poke_name)==True:
            choice_n.append(poke_name)
            choice.remove(poke_name)
    
        


    if len(choice)==0:
        st.write('しりとり終了')
        break

    poke=random.choice(choice)
    st.write(count,poke)
    count+=1

    