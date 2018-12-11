class SIGNATURE():

    # Checks for strings, imports, methods and symbols
    apkchecks = {"strings": [".apk", ".dex"]}

    rootchecks = {"strings": ["bin/su", "sudo", "superuser"]}

    apichecks = {
        "imports": [
            "nfc", "PackageInstaller", "bluetooth", "install",
            "PackageManager", "Datagram", "fingerprint"
        ],
        "methods": ["fingerprint", "bluetooth", "install", "package"],
        "symbols": ["fingerprint", "bluetooth", "install", "package"]
    }
    smschecks = {
        "imports": ["sms", "telephony"],
        "methods": [
            "sms", "telephony", "getDeviceId", "getSimOperator",
            "getSimCountry", "getImei"
        ],
        "symbols": [
            "sms", "telephony", "getDeviceId", "getSimOperator",
            "getSimCountry", "getImei"
        ]
    }
    locationchecks = {
        "imports":
        ["GoogleApiClient", "FusedLocationProvider", "setMockLocation"],
        "methods": [
            "getLastLocation", "getLocationAvailability",
            "requestLocationUpdates", "setMockLocation"
        ],
        "symbols": [
            "getLastLocation", "getLocationAvailability",
            "requestLocationUpdates"
        ]
    }
    netchecks = {
        "imports": ["http", "socket", "tcp", "udp"],
        "strings": ["client", "socket", "connect", "url", "uri"],
        "methods": ["connect", "send", "tcp", "udp"],
        "symbols": ["connect", "send", "tcp", "udp"]
    }

    urlchecks = {"strings": ["http:", "https:", "ftp:", "rtsp:"]}

    filechecks = {
        "imports": ["java/io/File"],
        "symbols": [
            "openFileOutputStream", "getFilesDir", "getCacheDir", "deleteFile",
            "getExternalStorageState", "isWritable", "setWritable"
        ],
        "strings": ["file:", "/tmp/", "/data/"]
    }
    cryptochecks = {
        "imports": ["crypt", "keystore", "cipher"],
        "methods": ["crypt", "cipher", "keystore"],
        "symbols": ["crypt", "cipher", "keystore"]
    }
    httpschecks = {"imports": ["javax/net/ssl"]}

    nativechecks = {
        "strings": ["loadLibrary"],
        "methods": ["loadLibrary"],
        "symbols": ["loadLibrary"]
    }
    camerachecks = {
        "imports":
        ["android/hardware/Camera", "android/hardware/Camera2", "camera"],
        "methods": ["camera", "takePicture"],
        "symbols": ["camera", "takePicture"]
    }

    audiochecks = {"imports": ["android/media/MediaRecorder", "MediaRecorder"]}

    emulatorchecks = {
        "imports": ["EmulatorDetector"],
        "strings": ["google_sdk", "init.goldfish.rc"],
        "methods": ["isEmulator"]
    }
    otherchecks = {
        "strings": [
            "api_key", "password", "pass", "admin", "secret", "encrypt",
            "decrypt"
        ],
        "methods":
        ["password", "pass", "admin", "secret", "encrypt", "decrypt"]
    }
