import streamlit as st
import re
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from sklearn.cluster import KMeans

def make_array(image):
    #making 3D array for project
    r_image = image[:,:,0].ravel()
    g_image = image[:,:,1].ravel()
    b_image = image[:,:,2].ravel()
    arr = r_image.reshape(r_image.shape[0],1)
    arr = np.hstack( (arr,g_image.reshape(g_image.shape[0],1)) )
    arr = np.hstack( (arr,b_image.reshape(b_image.shape[0],1)) )
    return arr
               

def project():
    st.title("COLOR PICKER 🎨")
    st.subheader('''This model is supposed to analyse an image provided and tries to pick given number of most noticible colors. ''')
    n = st.sidebar.selectbox("Select no of colors", [3,4,5])
    st.info('This model is still under work and will improve with time')
    up_file = st.file_uploader("Upload an image here")
    
    if up_file is not None:
        if "image" in up_file.type:
            f_type = re.search(r"\.\S+", up_file.name).group()
            f_type = f_type[1:].upper()
            st.image(up_file,width = 200)
            image = img.imread(up_file,format=f_type)
            arr = make_array(image)

            #fit model 
            model = KMeans(n_clusters=n,init='k-means++',tol = 0.01)
            pred = model.fit(arr)
            norm_centroids = pred.cluster_centers_ / 255 # for range 0-1
            st.write(f"Top {n} noticible colors")
            fig , ax = plt.subplots(nrows = 1, ncols= n)
            for i in range(n):
                ax[i].imshow([[norm_centroids[i]]])
                ax[i].axis('off')
            fig.tight_layout(pad=0)
            st.pyplot(fig)
            st.write('RGB values are :')
            st.write(f'{pred.cluster_centers_[0]}')

        else :
            st.error("File type not supported!")
      
