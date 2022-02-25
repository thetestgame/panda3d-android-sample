from setuptools import setup

# Necessary to switch Panda to the OpenGL ES 1 or 2 renderer
# pandagles2 supports shaders, but no fixed-function pipeline
# pandagles supports fixed-function pipeline, but no shaders
PRC_DATA = '''
load-display pandagles2
aux-display pandagles

notify-level info
gl-debug true
'''

setup(
    name="Asteroids",
    version="1.0.0",
    options={
        'build_apps': {
            # This field is required by Android and uniquely identifies the app.
            # It is usually based on the inverse of the developer's domain name
            # (e.g. "gamestudio.com" becomes "com.gamestudio"), followed by any
            # other components as needed to further identify the application.
            'application_id': 'org.panda3d.samples.asteroids',

            # This should be an integer that starts at 1 and is incremented with
            # every app update. This is just internal, whereas the ``version``
            # metadata field is used to show an arbitrary dot-separated version
            # string to the user. Every time you upload a new release to the
            # Play Console, this number must be updated.
            'android_version_code': 1,

            'gui_apps': {
                'asteroids': 'main.py',
            },
            'platforms': ['android'],
            'plugins': [
                # Note use of pandagles2/pandagles instead of pandagl
                'pandagles2',
                'pandagles',
                'p3openal_audio',
            ],
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            'extra_prc_data': PRC_DATA,

            # Required icon resolutions: 48x48, 72x72, 96x96, 144x144, 192x192
            # ..but make sure you author the logo in at least 512x512 since that
            # is the required resolution for the Play Store
            'icons': {'*': 'logo.png'},
        },

        'bdist_apps': {
            'signing_certificate': 'cert.pem',
            'signing_private_key': 'private.pem',
            # optional: Panda will otherwise ask passphrase on command-line
            'signing_passphrase': 'panda3d_is_cool',
        },
    },
    # Choosing a classifier in the Games category makes it marked a "Game"
    classifiers=['Topic :: Games/Entertainment'],
)
