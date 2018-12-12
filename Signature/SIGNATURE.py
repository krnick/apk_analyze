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
        "imports": [
            "GoogleApiClient", "FusedLocationProvider", "setMockLocation",
            "getLatitude", "getLastKnownLocation", "getCellLocation"
        ],
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

    internet = {
        "imports": [
            "openConnection", "isConnected", "getActiveNetworkInfo",
            "getConnectionInfo", "HttpClient.method.execute"
        ]
    }

    wifi_setting = {"imports": ["setWifiEnabled", "getScanResults","getMacAddress","getNetworkOperator"]}

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
        "imports":
        ["crypt", "keystore", "cipher", "MessageDigest.method.getInstance"],
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

    native_command = {"symbols": ["ProcessBuilder", "exec"]}
    dexclassloader = {
        "symbols": ["DexClassLoader", "loadClass", "MyClassLoader"]
    }

    process_kill = {"imports": ["killProcess"]}

    relection = {"imports": ["reflect", "reflect/Method.method.invoke"]}

    hooking = {"imports": ["setComponentEnabledSetting"]}

    system_evasion = {"strings": ["/proc/meminfo", "/proc/mounts"]}

    sensitive_information = {
        "strings": [
            "os", "android", "cpu", "imsi", "IMSI", "IMEI", "imei", "version",
            "sid", "appid", "phone"
        ]
    }
    query_operating_id = {
	"imports": ["Secure.method.getString"]
	}
