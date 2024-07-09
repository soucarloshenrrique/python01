os.makedirs(serve_dir, exist_ok=True)
os.makedirs(land_dir, exist_ok=True)
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None
min_visibility = 0.9
