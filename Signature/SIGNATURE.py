class SIGNATURE():

    # Checks for strings, imports, methods and symbols
    is_APK_checks = {"strings": [".apk", ".dex"]}

    is_ROOT_checks = {"strings": ["bin/su", "sudo", "superuser"]}

    is_API_checks = {
        "imports": [
            "nfc", "PackageInstaller", "bluetooth", "install",
            "PackageManager", "Datagram", "fingerprint"
        ],
        "methods": ["fingerprint", "bluetooth", "install", "package"],
        "symbols": ["fingerprint", "bluetooth", "install", "package"]
    }
    is_SMS_checks = {
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
    is_LOCATION_checks = {
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
    is_SOCKET_checks = {
        "imports": ["http", "socket", "tcp", "udp"],
        "strings": ["client", "socket", "connect", "url", "uri"],
        "methods": ["connect", "send", "tcp", "udp"],
        "symbols": ["connect", "send", "tcp", "udp"]
    }

    is_INTERNET_checks = {
        "imports": [
            "openConnection", "isConnected", "getActiveNetworkInfo",
            "getConnectionInfo", "HttpClient.method.execute"
        ]
    }

    is_WIFI_checks = {"imports": [
        "setWifiEnabled", "getScanResults", "getMacAddress", "getNetworkOperator"]}

    is_URL_checks = {"strings": ["http:", "https:", "ftp:", "rtsp:"]}

    is_FILE_checks = {
        "imports": ["java/io/File"],
        "symbols": [
            "openFileOutputStream", "getFilesDir", "getCacheDir", "deleteFile",
            "getExternalStorageState", "isWritable", "setWritable"
        ],
        "strings": ["file:", "/tmp/", "/data/"]
    }
    is_CRYPT_checks = {
        "imports":
        ["crypt", "keystore", "cipher", "MessageDigest.method.getInstance"],
        "methods": ["crypt", "cipher", "keystore"],
        "symbols": ["crypt", "cipher", "keystore"]
    }
    is_HTTPS_checks = {"imports": ["javax/net/ssl"]}

    is_CAMERA_checks = {
        "imports":
        ["android/hardware/Camera", "android/hardware/Camera2", "camera"],
        "methods": ["camera", "takePicture"],
        "symbols": ["camera", "takePicture"]
    }

    is_AUDIO_checks = {"imports": ["android/media/MediaRecorder", "MediaRecorder"]}

    is_EMULATOR_checks = {
        "imports": ["EmulatorDetector"],
        "strings": ["google_sdk", "init.goldfish.rc"],
        "methods": ["isEmulator"]
    }
    is_KEYPASSWORD_checks = {
        "strings": [
            "api_key", "password", "pass", "admin", "secret", "encrypt",
            "decrypt"
        ],
        "methods":
        ["password", "pass", "admin", "secret", "encrypt", "decrypt"]
    }

    is_NATIVE_checks = {"symbols": ["ProcessBuilder", "exec", "loadLibrary"], "imports": ["loadLibrary"], "methods": ["loadLibrary"]
                      }
    is_DEXCLASSLOAD_checks = {
        "symbols": ["DexClassLoader", "loadClass", "MyClassLoader"]
    }
    is_PROCESSKILL_checks = {"imports": ["killProcess"]}

    is_REFLECTION_checks = {"imports": ["reflect", "reflect/Method.method.invoke"]}

    is_HOOKING_checks = {"imports": ["setComponentEnabledSetting"]}

    is_SYSTEM_INFORMATION_checks = {"strings": ["/proc/meminfo", "/proc/mounts"]}

    is_SENSITIVE_INFORMATION_checks = {
        "strings": [
            "imsi", "IMSI", "IMEI", "imei","contact", "phonenumber", "phone"]
    }
    is_QUERY_OPERATING_ID_checks = {
        "imports": ["Secure.method.getString"]
    }
