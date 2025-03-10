import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="📟")
st.title(":blue[~~~Password Strength Checker~~~]",anchor=None)
st.divider()
#take password from user
password=st.text_input("Enter Your Password : " ,placeholder="Enter Minimum 8 characters" ,type="password")

#display Entered password
st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:4px; border-radius:5px; color:black; margin-bottom:14px;">
            Your Entered Password is: <b>{password}</b>
        </div>
        """, 
        unsafe_allow_html=True)

# strength Checking button 
strength_checker=st.button("Check Strength")



def password_strength_check(password):
    score=0
    rec1=" "
    rec2=" "
    rec3=" "
    rec4=" "
    rec5=" "
        #length checking
    if len(password) >= 8:
        score+=1
    else:
        rec1=":orange-background[:red[~Password Should be At least 8 characters Long]]"
       
    #Upper Case
    if  re.search(r'[A-Z]',password):
        score+=1
    else:
        rec2=":orange-background[:red[~Password should contain at Least one Upper Case Letter]]"
    #lower Case
    if  re.search(r'[a-z]',password):
        score+=1
    else:
        rec3=":orange-background[:red[~Password should contain at Least one Lower Case Letter]]"
        
    #0-9 digits
    if  re.search(r'\d',password):
        score+=1
    else:
        rec4=":orange-background[:red[~Password should contain at Least one Number (0-9)]]"
  
    #special Characters
    if re.search(r'[!@#$%^&*><)(.,_-]',password):
        score+=1
    else:
        rec5=":orange-background[:red[~Password should contain at Least one Special Character (!@#$%^&*)]]"
       

        #How Strong The Password Is?
    st.header('Results :')

        #score
    st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:10px; border-radius:5px; color:black; margin-bottom:14px;">
            Score of your Password is : <b style="color:#08556E;">{score}</b>
        </div>
        """, 
        unsafe_allow_html=True)

        #Statement Based on Score 
        #Weak
    if score == 1 or score == 2:
            st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:10px; border-radius:5px; color:black; margin-bottom:14px;">
            Password's Strength is : <b style="color:#08556E;">Weak </b>
        </div>
        """, 
        unsafe_allow_html=True)
            
            st.header('Recommendations : ')
            st.markdown(rec1)
            st.markdown(rec2)
            st.markdown(rec3)
            st.markdown(rec4)
            st.markdown(rec5)
            
        #Moderate
    elif score == 3 or score == 4:
            st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:10px; border-radius:5px; color:black; margin-bottom:14px;">
            Password's Strength is : <b style="color:#08556E;">Moderate </b>
        </div>
        """, 
        unsafe_allow_html=True)
            
            st.header('Recommendations : ')
            st.markdown(rec1)
            st.markdown(rec2)
            st.markdown(rec3)
            st.markdown(rec4)
            st.markdown(rec5)
            
            
        #Strong
    elif score == 5:
            st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:10px; border-radius:5px; color:black; margin-bottom:14px;">
            Password's Strength is : <b style="color:#08556E;">Strong </b>
        </div>
        """, 
        unsafe_allow_html=True)
            
            st.header('Recommendations : ')
            st.markdown(f"""
        <div style="background-color:#CAE7F4; padding:10px; border-radius:5px; color:black; margin-bottom:14px;">
            Great! You Typed a <b style="color:#0B8F35;">Secure </b> Password </div>
        """, 
        unsafe_allow_html=True)
            
    
   
        




if strength_checker == True :
    password_strength_check(password)
