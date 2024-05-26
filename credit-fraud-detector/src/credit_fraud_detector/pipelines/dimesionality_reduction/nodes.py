import pandas as pd
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA, TruncatedSVD
import time

def apply_dimensionality_reduction(X: pd.DataFrame) -> dict:
    result = {}
    
    t0 = time.time()
    result['tsne'] = TSNE(n_components=2, random_state=42).fit_transform(X.values)
    result['tsne_time'] = time.time() - t0
    
    t0 = time.time()
    result['pca'] = PCA(n_components=2, random_state=42).fit_transform(X.values)
    result['pca_time'] = time.time() - t0
    
    t0 = time.time()
    result['svd'] = TruncatedSVD(n_components=2, algorithm='randomized', random_state=42).fit_transform(X.values)
    result['svd_time'] = time.time() - t0
    
    return result
