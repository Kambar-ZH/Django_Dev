
VIDEO_TEMPLATE_FILE_ALLOWED_EXTENSIONS = ('.mp4', '.mov', '.webm', '.mpeg')
# 10 MB
VIDEO_TEMPLATE_MAX_FILE_SIZE = 10 * 1024 * 1024

IMAGE_ALLOWED_EXTENSIONS = ('.jpg', '.png')
# 10 MB
IMAGE_MAX_FILE_SIZE = 10 * 1024 * 1024

ALGORITHMS = 1
INTERVIEW = 2
GAME_DEV = 3
BACKEND_DEV = 4
FRONTEND_DEV = 5
ANDROID_DEV = 6
IOS_DEV = 7

COURSE_CATEGORIES = (
    (ALGORITHMS, 'algorithms'),
    (INTERVIEW, 'interview'),
    (GAME_DEV, 'game development'),
    (BACKEND_DEV, 'backend development'),
    (FRONTEND_DEV, 'frontend development'),
    (ANDROID_DEV, 'android development'),
    (IOS_DEV, 'ios development'),
)