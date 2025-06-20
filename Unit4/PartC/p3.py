from collections import deque


def track_scene_transitions(scenes):
    queue = deque(scenes)
    while len(queue) > 1:
        current_scene = queue.popleft()
        next_scene = queue[0]
        print(f"Transitioning from '{current_scene}' to '{next_scene}'")


scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)
scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)
