# ====================== ENHANCED ROM BUILD DETECTION CATEGORIES ======================
DETECTION_LEVELS = {
    "CRITICAL": {
        "color": "#e17055",
        "icon": "🔥",
        "keywords": ["critical", "fatal", "crash", "segfault", "abort", "killed", "terminated"],
        "patterns": [
            r"\bcritical\b", r"\bfatal\b", r"\bcrash\b", r"\bsegfault\b", 
            r"killed by signal", r"terminated", r"abort\(\)"
        ]
    },
    
    "BUILD_FAILED": {
        "color": "#d63031",
        "icon": "💥",
        "keywords": ["build failed", "compilation failed", "make failed", "ninja failed"],
        "patterns": [
            r"build failed", r"compilation.*failed", r"make.*failed", 
            r"ninja.*failed", r"build/core.*error", r"\[.*FAILED.*\]",
            r"recipe for target.*failed", r"Stop\.", r"make: \*\*\*"
        ]
    },
    
    "DEPENDENCY_MISSING": {
        "color": "#fd79a8", 
        "icon": "📦",
        "keywords": ["not found", "no such file", "missing", "undefined reference"],
        "patterns": [
            r"No such file or directory", r"not found", r"missing",
            r"undefined reference", r"cannot find", r"does not exist",
            r"No rule to make target", r"Nothing to be done",
            r"ld: cannot find", r"fatal error:.*not found"
        ]
    },
    
    "KERNEL_ERROR": {
        "color": "#e84393",
        "icon": "🔧",
        "keywords": ["kernel", "dtb", "defconfig", "zimage", "image.gz"],
        "patterns": [
            r"kernel.*error", r"defconfig.*not found", r"dtb.*failed",
            r"zImage.*failed", r"Image\.gz.*failed", r"boot\.img.*failed",
            r"kernel/.*error", r"arch/arm.*error", r"drivers/.*error",
            r"CONFIG_.*not set", r"warning: #warning"
        ]
    },
    
    "VENDOR_BLOBS": {
        "color": "#a29bfe",
        "icon": "🏭", 
        "keywords": ["proprietary", "vendor", "blobs", "extract-files"],
        "patterns": [
            r"proprietary.*missing", r"vendor.*not found", r"blobs.*missing",
            r"extract-files.*failed", r"proprietary-files\.txt.*error",
            r"vendor/.*not found", r"firmware.*missing"
        ]
    },
    
    "MANIFEST_SYNC": {
        "color": "#00cec9",
        "icon": "🔄",
        "keywords": ["repo sync", "manifest", "git", "fetch", "checkout"],
        "patterns": [
            r"repo sync.*failed", r"manifest.*error", r"git.*failed",
            r"fatal: .*git", r"error: .*checkout", r"Fetching project",
            r"Checking out files", r"error: RPC failed"
        ]
    },
    
    "SEPOLICY_ERROR": {
        "color": "#fdcb6e",
        "icon": "🔒",
        "keywords": ["sepolicy", "selinux", "policy", "security"],
        "patterns": [
            r"sepolicy.*error", r"selinux.*denied", r"policy.*failed",
            r"security.*violation", r"avc:.*denied", r"sepolicy_tests",
            r"neverallow.*violation", r"checkpolicy.*failed"
        ]
    },
    
    "GAPPS_ISSUES": {
        "color": "#fab1a0",
        "icon": "📱",
        "keywords": ["gapps", "google", "play store", "gsf", "gms"],
        "patterns": [
            r"gapps.*failed", r"google.*service.*failed", r"play.*store.*error",
            r"gsf.*failed", r"gms.*error", r"com\.google\..*failed",
            r"GoogleServicesFramework", r"Phonesky.*failed"
        ]
    },
    
    "TREBLE_COMPATIBILITY": {
        "color": "#00b894",
        "icon": "🌳",
        "keywords": ["treble", "vndk", "vendor interface", "hal"],
        "patterns": [
            r"treble.*error", r"vndk.*failed", r"vendor.*interface.*error",
            r"hal.*failed", r"vintf.*error", r"compatibility.*failed",
            r"BOARD_VNDK_VERSION", r"system.*as.*root"
        ]
    },
    
    "MEMORY_SPACE": {
        "color": "#e17055",
        "icon": "💾",
        "keywords": ["no space", "memory", "disk full", "out of memory"],
        "patterns": [
            r"no space left", r"disk.*full", r"out of memory", r"malloc.*failed",
            r"cannot allocate memory", r"virtual memory exhausted",
            r"No space left on device", r"Disk quota exceeded"
        ]
    },
    
    "PERMISSION_DENIED": {
        "color": "#fd79a8",
        "icon": "🚫", 
        "keywords": ["permission denied", "access denied", "not permitted"],
        "patterns": [
            r"permission denied", r"access denied", r"not permitted",
            r"operation not permitted", r"insufficient privileges",
            r"you don't have permission", r"sudo.*required"
        ]
    },
    
    "COMPILER_ERROR": {
        "color": "#d63031",  
        "icon": "⚡",
        "keywords": ["error:", "undefined", "redefinition", "declaration"],
        "patterns": [
            r"error:.*undeclared", r"error:.*undefined", r"error:.*redefinition",
            r"error:.*declaration", r"error:.*syntax", r"error:.*expected",
            r"compilation terminated", r"too many errors emitted",
            r"\berror\b.*:\s*\d+"
        ]
    },
    
    "CLANG_LLVM": {
        "color": "#a29bfe",
        "icon": "🔨",
        "keywords": ["clang", "llvm", "linker", "ld.lld"],
        "patterns": [
            r"clang.*error", r"llvm.*error", r"ld\.lld.*failed",
            r"linker.*error", r"lld.*failed", r"clang\+\+.*failed",
            r"undefined symbol", r"duplicate symbol", r"relocation.*failed"
        ]
    },
    
    "JACK_COMPILATION": {
        "color": "#fd79a8",
        "icon": "☕",
        "keywords": ["jack", "jill", "dex", "r8"],
        "patterns": [
            r"jack.*failed", r"jill.*error", r"dex.*failed", 
            r"r8.*failed", r"proguard.*failed", r"dx.*failed",
            r"Jack server.*failed", r"OutOfMemoryError.*Jack"
        ]
    },
    
    "OTA_PACKAGE": {
        "color": "#00cec9",
        "icon": "📦",
        "keywords": ["ota", "update", "recovery", "zip"],
        "patterns": [
            r"ota.*failed", r"update.*package.*failed", r"recovery.*failed",
            r"zip.*alignment.*failed", r"signing.*failed", r"verification.*failed",
            r"META-INF.*error", r"updater-script.*error"
        ]
    },
    
    "DEVICE_SPECIFIC": {
        "color": "#fdcb6e",
        "icon": "📱",
        "keywords": ["board", "device", "init", "rc file"],
        "patterns": [
            r"BoardConfig.*error", r"device.*mk.*error", r"init.*rc.*error",
            r"device specific.*failed", r"hardware.*not found", 
            r"overlay.*failed", r"device tree.*error"
        ]
    },
    
    "SOONG_BUILD": {
        "color": "#6c5ce7",
        "icon": "🏗️", 
        "keywords": ["soong", "blueprint", "android.bp"],
        "patterns": [
            r"soong.*failed", r"blueprint.*error", r"Android\.bp.*error",
            r"soong_ui.*failed", r"build system.*error", r"bootstrap.*failed",
            r"ninja.*build.*stopped"
        ]
    },
    
    "WARNING": {
        "color": "#fdcb6e",
        "icon": "⚠️",
        "keywords": ["warn", "unable", "cannot", "deprecated", "not found"],
        "patterns": [
            r"\bwarn(?:ing)?\b", r"\bcannot\b", r"\bdeprecated\b",
            r"note:", r"warning:", r"deprecated"
        ]
    },
    
    "INFO": {
        "color": "#74b9ff",
        "icon": "ℹ️",
        "keywords": ["info", "notice", "debug", "trace", "building"],
        "patterns": [r"\binfo\b", r"\bnotice\b", r"\bdebug\b", r"Building"]
    },
    
    "SUCCESS_INDICATORS": {
        "color": "#00b894",
        "icon": "✅",
        "keywords": ["successful", "completed", "finished", "done"],
        "patterns": [
            r"build.*successful", r"compilation.*completed", r"finished",
            r".*done\.", r"Build completed", r"Package complete"
        ]
    }
}

# ====================== ROM BUILD SPECIFIC MESSAGES ======================
def generate_rom_message(level, line):
    """Generate contextual messages for ROM building issues"""
    messages = {
        "CRITICAL": "Critical system failure - build process terminated",
        "BUILD_FAILED": "Build compilation failed - check dependencies and code",
        "DEPENDENCY_MISSING": "Missing dependencies or files - may need to sync sources",
        "KERNEL_ERROR": "Kernel compilation issue - check defconfig and device tree", 
        "VENDOR_BLOBS": "Proprietary vendor files missing - run extract-files.sh",
        "MANIFEST_SYNC": "Repository sync issue - check network and manifest",
        "SEPOLICY_ERROR": "SELinux policy violation - update sepolicy rules",
        "GAPPS_ISSUES": "Google Apps integration failed - check GApps package compatibility",
        "TREBLE_COMPATIBILITY": "Project Treble compatibility issue - check VNDK version",
        "MEMORY_SPACE": "Insufficient disk space or memory - clean build directory",
        "PERMISSION_DENIED": "Permission error - check file ownership and access rights",
        "COMPILER_ERROR": "Code compilation error - fix syntax or missing declarations",
        "CLANG_LLVM": "Clang/LLVM toolchain error - check compiler configuration",
        "JACK_COMPILATION": "Java compilation failed - may need to increase heap size",
        "OTA_PACKAGE": "Update package creation failed - check signing keys",
        "DEVICE_SPECIFIC": "Device-specific configuration error - check BoardConfig.mk",
        "SOONG_BUILD": "Modern build system error - check Android.bp files",
        "WARNING": "Potential issue identified",
        "INFO": "Build process information",
        "SUCCESS_INDICATORS": "Build step completed successfully"
    }
    return messages.get(level, "ROM build issue detected")

# ====================== ENHANCED PATTERN MATCHING ======================
def detect_rom_issues(line, line_num):
    """Enhanced ROM-specific issue detection with context"""
    issues = []
    line_lower = line.lower()
    
    # Special context-aware detection
    context_patterns = {
        # Detect specific Android build errors
        "VENDOR_BLOBS": [
            r"proprietary.*missing.*extract.*sh",
            r"vendor.*img.*not.*found", 
            r"system.*extract.*failed"
        ],
        
        # Kernel specific patterns
        "KERNEL_ERROR": [
            r"make.*arch.*arm.*failed",
            r"scripts/dtc.*failed",
            r"drivers.*\.ko.*failed"
        ],
        
        # Memory related issues during build
        "MEMORY_SPACE": [
            r"cc1.*out.*of.*memory",
            r"ld.*memory.*exhausted",
            r"ninja.*memory.*allocation"
        ],
        
        # Specific to modern Android builds
        "SOONG_BUILD": [
            r"out/soong.*build.*ninja.*failed",
            r"soong_ui.*Kati.*failed",
            r"combined.*ninja.*files.*failed"
        ]
    }
    
    # Check context patterns first
    for level, patterns in context_patterns.items():
        if any(re.search(pattern, line, re.IGNORECASE) for pattern in patterns):
            issues.append({
                "line_num": line_num,
                "line": line.strip(),
                "level": level,
                "icon": DETECTION_LEVELS[level]["icon"],
                "message": generate_rom_message(level, line),
                "context": "ROM Build Specific"
            })
            continue
    
    # If no context match, use standard detection
    if not issues:
        for level, config in DETECTION_LEVELS.items():
            # Check keywords
            keyword_match = any(kw in line_lower for kw in config["keywords"])
            
            # Check regex patterns  
            pattern_match = any(re.search(ptn, line, re.IGNORECASE) for ptn in config["patterns"])
            
            if keyword_match or pattern_match:
                issues.append({
                    "line_num": line_num,
                    "line": line.strip(),
                    "level": level,
                    "icon": config["icon"],
                    "message": generate_rom_message(level, line),
                    "context": "Standard Detection"
                })
                break  # Only detect first match to avoid duplicates
    
    return issues

# ====================== ROM BUILD TIPS ======================
ROM_BUILD_TIPS = {
    "DEPENDENCY_MISSING": [
        "Run 'repo sync --force-sync' to update all repositories",
        "Check if device-specific repositories are properly added to manifest",
        "Verify all proprietary files are extracted with extract-files.sh"
    ],
    
    "KERNEL_ERROR": [
        "Clean kernel with 'make mrproper' in kernel directory", 
        "Check if correct defconfig is being used for your device",
        "Verify device tree source files are present and correct"
    ],
    
    "VENDOR_BLOBS": [
        "Run ./extract-files.sh from device directory",
        "Use adb pull to manually extract missing proprietary files",
        "Check if device is properly rooted for blob extraction"
    ],
    
    "MEMORY_SPACE": [
        "Clean build directory with 'make clean' or 'rm -rf out/'",
        "Increase swap space or use faster storage",
        "Use 'make -j$(nproc)' instead of higher parallel jobs"
    ],
    
    "SEPOLICY_ERROR": [
        "Update sepolicy rules in device/manufacturer/device/sepolicy/",
        "Check for missing sepolicy entries in system/sepolicy/",
        "Verify contexts and permissions in file_contexts"
    ]
}