import base64
import io
from PIL import Image
import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load and preprocess data
digits = datasets.load_digits()
X = digits.data
y = digits.target

# PCA to 2D
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

# Clustering
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(X)

def image_to_base64(image_array):
    arr = (image_array.reshape(8, 8) * 16).astype(np.uint8)  # fix scaling
    img = Image.fromarray(arr)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

images_base64 = [image_to_base64(img) for img in X]

app = dash.Dash(__name__)
server = app.server

# Plot
fig = px.scatter(
    x=X_pca[:, 0],
    y=X_pca[:, 1],
    color=clusters,
    color_discrete_sequence=px.colors.qualitative.Plotly,
    title="PCA Projection of Image Embeddings",
    labels={'color': 'Cluster'},
)

fig.update_traces(
    marker=dict(size=6, opacity=0.7),
    customdata=images_base64
)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        namelength=-1
    )
)

app.layout = html.Div([
    html.H1("Image Embedding Clusters", style={'textAlign': 'center'}),
    dcc.Graph(id='cluster-plot', figure=fig),

    html.Div([
        html.Img(
            id='hover-image',
            src='',
            style={
                'width': '100px',
                'height': '100px',
                'border': '1px solid #ddd',
                'borderRadius': '4px',
                'padding': '5px',
                'display': 'none'
            }
        )
    ], style={'textAlign': 'center'})
])

@app.callback(
    Output('hover-image', 'src'),
    Output('hover-image', 'style'),
    Input('cluster-plot', 'hoverData')
)
def display_image(hoverData):
    if hoverData is None:
        return '', {'display': 'none'}

    point = hoverData['points'][0]
    img_src = "data:image/png;base64," + point['customdata']

    return img_src, {'display': 'block'}

if __name__ == '__main__':
    app.run_server(debug=True)
