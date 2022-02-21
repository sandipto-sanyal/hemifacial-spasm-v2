import streamlit as st
# from datetime import datetime
import base64
import constants as c


def open_local_gifs(path:str):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

st.set_page_config(page_title='Hemifacial Spasm Journey', 
                   page_icon=c.favicon, 
                   layout="wide", 
                   initial_sidebar_state="auto", 
                   menu_items=None
                   )
# add_selectbox = st.sidebar.slider(label = 'Timeline',
#                                   min_value=2017,
#                                   max_value=2022
#                                   )
st.header('My Journey with Hemifacial Spasm', anchor='a')
st.header('2017 - How it started', 
          # anchor='h1'
          )
st.write(c.start)
st.image(c.twitching_gif,caption='Eye Twitch', width=250)
st.write(c.reaction)

st.header("Progress",
          # anchor='h2'
          )
st.write(c.progress)

st.header('2018 - Eye Consultation with [Dr. Dipankar Roy](%s)' % c.dipankar_roy_link, 
          # anchor='h3'
          )
st.write(c.eye_consultation1 % c.dipankar_roy_link)
st.write(c.eye_consultation1_reaction)

st.header('2019 - Eye Consultation with [Dr. Somnath Majumdar](%s)' % c.somnath_majumdar_link, 
          # anchor='h4'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://fortiskolkata.com/assets/uploads/doctors/dr%20somnath.jpg',
             caption='Dr. Somnath Majumdar',
             width=175)
with col2:
    st.write(c.eye_consultation2)
st.write(c.eye_consultation2_reaction)
st.image(c.hfs_gif,caption="My Condition", width=250)


st.header('2019 - Eye Consultation at [LV Prasad Eye Institute](%s)' % c.lvpei_link, 
          # anchor='h5'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://avocure-uploads.s3.amazonaws.com/uploads/clinic/cover_pic_url/122/dr-taraprasad-das-lv-prasad-eye-institute--banjara-hills-hyderabad-ophthalmologists-2rd1m.jpg',
             caption='LV Prasad Eye Institute Hyderabad',
             width=325)
with col2:
    st.write(c.eye_consultation3)
st.write(c.eye_consultation3_reaction)
st.image(c.tension_gif,caption='Tension',width=250)

st.header('2019 - Neurology Counsultation at [Care Hospital Hi-Tech City](%s)' % c.care_hospital_link, 
          # anchor='h6'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://www.carehospitals.com/wp-content/uploads/2018/09/Dr.-JMK-Murthy.png',
             caption='Dr. J M K Murthy Care Hospital Hi-Tech City Hyderabad',
             width=250)
with col2:
    st.write(c.neuro_consultation1 % c.jmk_murthy_link)
st.write(c.neuro_consultation1_reaction)
st.image(c.tension_gif2, caption='More Tension', width=250)


st.header('2019 - Yoga Therapy Consultation with [Prem Sundar Das](%s)' % c.ps_das_link, 
          # anchor='h7'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://psdasyogapathy.org/images/ps.jpg',
             caption='Dr. Prem Sundar Das - PS Das Yogapathy',
             width=175)
with col2:
    st.write(c.ps_das_consultation % c.ps_das_link)
st.write(c.ps_das_consultation_reaction)
# data_url = open_local_gifs(path="./media/hfs_before.gif")
# st.image(data_url,caption='Current Condtion',width=250
# )
st.video(data='./media/hfs_before.mp4')

st.header('2020 - Neurology Consultation with [Dr. Anshuman Mukherjee]({}) and [Dr. Trishit Roy]({})'.format(c.anshuman_link, c.trishit_link),
          # anchor='h8'
          )
col1, col2, col3 = st.columns(3)
with col1:
    st.image('https://www.docton.in/upload/doctor_files/doctordoc_1566729500.jpg',
             caption='Dr. Anshuman Mukherjee - Neurologist',
             width=275)
    
with col2:
    st.image('./media/trishit.png',
             caption='Dr. Trishit Roy - Neurologist',
             width=275)
with col3:
    st.write(c.neuro_consultation2)
st.write(c.neuro_consultation2_reaction)


st.header('2020 - Homeopathy Consultation with [Dr. Anirban Sukul]({})'.format(c.anirban_link),
          # anchor='h9'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://www.sukulhomeopathy.com/images/anirban_sukul.gif',
             caption='Dr. Anirban Sukul - Homeopath',
             width=375)
with col2:
    st.write(c.homeopathy_consultation.format(c.nimhans_link))
st.write(c.homeopathy_consultation_reaction)


st.header('2020 - Consultation at [NIMHANS]({})'.format(c.nimhans_link),
          # anchor='h10'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2020/06/21/nimhans-1592754868.jpg?itok=fOpKnBu3',
             caption='National Institute of Mental Health and Neuro Sciences (NIMHANS)',
             width=350)
with col2:
    st.write(c.nimhans_consultation.format(c.ink_link))
st.write(c.nimhans_consultation_reaction)

st.header('2020 - Consultation at [Institute of Neurosciences Kolkata]({})'.format(c.ink_link),
          # anchor='h11'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://content3.jdmagicbox.com/comp/kolkata/s6/033pxx33.xx33.090718221238.q4s6/catalogue/institute-of-neurosciences-kolkata-park-circus-kolkata-orthopaedic-doctors-bsm4z.jpg?clr=5a460c',
             caption='Institute Of Neurosciences Kolkata',
             width=425)
with col2:
    st.write(c.ink_consultation.format(c.ampba_link, c.dk_pradhan_link))
st.write(c.ink_consultation_reaction)
st.image(image=c.study_gif,caption='Study Time',width=250)

st.header('10th February 2022 - Micro Vascular Decompression Surgery at [Institute of Neurosciences Kolkata]({})'.format(c.ink_link),
          # anchor='h12'
          )
col1, col2 = st.columns(2)
with col1:
    st.image('https://neurokolkata.org/wp-content/uploads/2019/01/doctor4_-213x230.png',
             caption='Dr. Dipendra Kumar Pradhan - Institute of Neurosciences Kolkata',
             width=175)
    st.image('https://neurokolkata.org/wp-content/uploads/2018/11/Dr.-Partha-Ghosh-213x230.png',
             caption='Dr. Partha Ghosh - Institute of Neurosciences Kolkata',
             width=175)
with col2:
    st.write(c.ink_surgery.format(c.dk_pradhan_link,c.partha_ghosh_link))
    st.image(c.surgery_gif,width=350)
st.write(c.ink_stay_experience.format(c.apollo_sindoori_link))
st.image(c.yummy_gif,width=250)

st.header('19 February 2022 - Final thoughts',
          # anchor='h12'
          )
st.write(c.final_thoughts)

st.header('Key Takeaways')
st.write(c.key_takeaways)


col1, col2 = st.columns(2)
with col1:
    st.subheader('Before')
    st.video('./media/hfs_before.mp4')
with col2:
    st.subheader('After')
    st.video('./media/hfs_after.mp4')