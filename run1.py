# ===== File: rom_detection_levels.py =====
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

# ===== File: run.py =====
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import os
from datetime import datetime
import re
from rom_detection_levels import detect_rom_issues, DETECTION_LEVELS

# ====================== MODERN UI THEME ======================
class ModernTheme:
    # Orchis-inspired color palette
    COLORS = {
        'bg_primary': '#1a1a1a',
        'bg_secondary': '#2d2d2d', 
        'bg_tertiary': '#3d3d3d',
        'accent': '#6c5ce7',
        'accent_light': '#a29bfe',
        'accent_dark': '#5f3dc4',
        'text_primary': '#ffffff',
        'text_secondary': '#b2bec3',
        'text_muted': '#636e72',
        'success': '#00b894',
        'warning': '#fdcb6e',
        'error': '#e17055',
        'info': '#74b9ff',
        'border': '#4a4a4a',
        'shadow': '#0d1117'
    }
    
    FONTS = {
        'header': ('Segoe UI', 14, 'bold'),
        'subheader': ('Segoe UI', 12, 'bold'),
        'body': ('Segoe UI', 10),
        'mono': ('JetBrains Mono', 10),
        'mono_bold': ('JetBrains Mono', 10, 'bold')
    }

class ModernButton(tk.Frame):
    def __init__(self, parent, text, command=None, style="primary", **kwargs):
        super().__init__(parent, **kwargs)
        self.command = command
        self.style = style
        self.text = text
        
        # Button colors based on style
        styles = {
            "primary": {
                "bg": ModernTheme.COLORS['accent'],
                "hover_bg": ModernTheme.COLORS['accent_light'],
                "text": ModernTheme.COLORS['text_primary']
            },
            "secondary": {
                "bg": ModernTheme.COLORS['bg_tertiary'],
                "hover_bg": ModernTheme.COLORS['border'],
                "text": ModernTheme.COLORS['text_primary']
            },
            "success": {
                "bg": ModernTheme.COLORS['success'],
                "hover_bg": "#00a085",
                "text": ModernTheme.COLORS['text_primary']
            }
        }
        
        self.style_config = styles.get(style, styles["primary"])
        self.setup_button()
    
    def setup_button(self):
        self.configure(
            bg=self.style_config["bg"],
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )
        
        self.label = tk.Label(
            self,
            text=self.text,
            bg=self.style_config["bg"],
            fg=self.style_config["text"],
            font=ModernTheme.FONTS['body'],
            pady=8,
            padx=16
        )
        self.label.pack(fill="both", expand=True)
        
        # Bind events
        for widget in [self, self.label]:
            widget.bind("<Button-1>", self.on_click)
            widget.bind("<Enter>", self.on_enter)
            widget.bind("<Leave>", self.on_leave)
    
    def on_click(self, event):
        if self.command:
            self.command()
    
    def on_enter(self, event):
        self.configure(bg=self.style_config["hover_bg"])
        self.label.configure(bg=self.style_config["hover_bg"])
    
    def on_leave(self, event):
        self.configure(bg=self.style_config["bg"])
        self.label.configure(bg=self.style_config["bg"])

class ModernCard(tk.Frame):
    def __init__(self, parent, title="", **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(
            bg=ModernTheme.COLORS['bg_secondary'],
            relief="flat",
            bd=1,
            highlightbackground=ModernTheme.COLORS['border'],
            highlightthickness=1
        )
        
        if title:
            title_label = tk.Label(
                self,
                text=title,
                bg=ModernTheme.COLORS['bg_secondary'],
                fg=ModernTheme.COLORS['text_primary'],
                font=ModernTheme.FONTS['subheader'],
                anchor="w"
            )
            title_label.pack(fill="x", padx=16, pady=(16, 8))

class EnhancedLogSeeker:
    def __init__(self, root):
        self.root = root
        self.setup_theme()
        self.setup_ui()
        self.setup_logging()
        self.current_file = ""
        self.current_results = []
        self.animation_after_id = None
        
    def setup_theme(self):
        """Setup modern dark theme"""
        self.root.configure(bg=ModernTheme.COLORS['bg_primary'])
        
        # Configure ttk styles
        style = ttk.Style()
        
        # Try to set a modern theme
        try:
            style.theme_use('clam')
        except:
            pass
        
        # Configure custom styles
        style.configure('Modern.TEntry',
            fieldbackground=ModernTheme.COLORS['bg_secondary'],
            background=ModernTheme.COLORS['bg_secondary'],
            foreground=ModernTheme.COLORS['text_primary'],
            bordercolor=ModernTheme.COLORS['border'],
            lightcolor=ModernTheme.COLORS['border'],
            darkcolor=ModernTheme.COLORS['border'],
            insertcolor=ModernTheme.COLORS['accent'],
            selectbackground=ModernTheme.COLORS['accent'],
            selectforeground=ModernTheme.COLORS['text_primary'])
        
        style.configure('Modern.TCombobox',
            fieldbackground=ModernTheme.COLORS['bg_secondary'],
            background=ModernTheme.COLORS['bg_secondary'],
            foreground=ModernTheme.COLORS['text_primary'],
            bordercolor=ModernTheme.COLORS['border'],
            arrowcolor=ModernTheme.COLORS['text_secondary'],
            selectbackground=ModernTheme.COLORS['accent'])
        
        style.map('Modern.TCombobox',
            selectbackground=[('focus', ModernTheme.COLORS['accent'])],
            selectforeground=[('focus', ModernTheme.COLORS['text_primary'])])

    def setup_logging(self):
        """Configure logging"""
        log_dir = os.path.join(os.path.expanduser('~'), '.enhanced_log_seeker')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            filename=os.path.join(log_dir, 'app.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Enhanced Log Seeker started")

    def setup_ui(self):
        """Modern UI with cards and smooth design"""
        self.root.title("🔍 Enhanced Log Seeker v3.0")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Main container with padding
        main_frame = tk.Frame(
            self.root, 
            bg=ModernTheme.COLORS['bg_primary'],
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Control panel card
        self.create_control_panel(main_frame)
        
        # Stats panel
        self.create_stats_panel(main_frame)
        
        # Results area
        self.create_results_area(main_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create modern header"""
        header_frame = tk.Frame(parent, bg=ModernTheme.COLORS['bg_primary'])
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Title with gradient effect simulation
        title_label = tk.Label(
            header_frame,
            text="🔍 Enhanced Log Seeker",
            bg=ModernTheme.COLORS['bg_primary'],
            fg=ModernTheme.COLORS['accent'],
            font=('Segoe UI', 24, 'bold')
        )
        title_label.pack(side="left")
        
        # Version badge
        version_frame = tk.Frame(
            header_frame,
            bg=ModernTheme.COLORS['accent'],
            relief="flat"
        )
        version_frame.pack(side="right", padx=(0, 0))
        
        version_label = tk.Label(
            version_frame,
            text="v3.0",
            bg=ModernTheme.COLORS['accent'],
            fg=ModernTheme.COLORS['text_primary'],
            font=ModernTheme.FONTS['body'],
            padx=8,
            pady=4
        )
        version_label.pack()
    
    def create_control_panel(self, parent):
        """Create modern control panel"""
        control_card = ModernCard(parent, title="📁 File Analysis")
        control_card.pack(fill="x", pady=(0, 16))
        
        # File selection row
        file_frame = tk.Frame(control_card, bg=ModernTheme.COLORS['bg_secondary'])
        file_frame.pack(fill="x", padx=16, pady=8)
        
        tk.Label(
            file_frame,
            text="Select File:",
            bg=ModernTheme.COLORS['bg_secondary'],
            fg=ModernTheme.COLORS['text_secondary'],
            font=ModernTheme.FONTS['body']
        ).pack(side="left", padx=(0, 8))
        
        self.file_var = tk.StringVar()
        self.file_entry = ttk.Entry(
            file_frame,
            textvariable=self.file_var,
            style='Modern.TEntry',
            font=ModernTheme.FONTS['mono'],
            width=50
        )
        self.file_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        
        browse_btn = ModernButton(
            file_frame,
            text="📂 Browse",
            command=self.browse_file,
            style="secondary"
        )
        browse_btn.pack(side="right", padx=(8, 0))
        
        # Filter and action row
        action_frame = tk.Frame(control_card, bg=ModernTheme.COLORS['bg_secondary'])
        action_frame.pack(fill="x", padx=16, pady=(0, 16))
        
        # Filter section
        filter_frame = tk.Frame(action_frame, bg=ModernTheme.COLORS['bg_secondary'])
        filter_frame.pack(side="left")
        
        tk.Label(
            filter_frame,
            text="Filter Level:",
            bg=ModernTheme.COLORS['bg_secondary'],
            fg=ModernTheme.COLORS['text_secondary'],
            font=ModernTheme.FONTS['body']
        ).pack(side="left", padx=(0, 8))
        
        self.filter_var = tk.StringVar(value="ALL")
        self.filter_menu = ttk.Combobox(
            filter_frame,
            textvariable=self.filter_var,
            values=["ALL"] + list(DETECTION_LEVELS.keys()),
            state="readonly",
            style='Modern.TCombobox',
            width=15
        )
        self.filter_menu.pack(side="left")
        self.filter_menu.bind('<<ComboboxSelected>>', lambda e: self.filter_results())
        
        # Action buttons
        action_buttons = tk.Frame(action_frame, bg=ModernTheme.COLORS['bg_secondary'])
        action_buttons.pack(side="right")
        
        self.analyze_btn = ModernButton(
            action_buttons,
            text="🔍 Analyze",
            command=self.analyze_file,
            style="primary"
        )
        self.analyze_btn.pack(side="left", padx=(0, 8))
        
        self.export_btn = ModernButton(
            action_buttons,
            text="💾 Export",
            command=self.export_results,
            style="success"
        )
        self.export_btn.pack(side="left")
        
    def create_stats_panel(self, parent):
        """Create statistics panel"""
        self.stats_card = ModernCard(parent, title="📊 Analysis Statistics")
        self.stats_card.pack(fill="x", pady=(0, 16))
        
        stats_frame = tk.Frame(self.stats_card, bg=ModernTheme.COLORS['bg_secondary'])
        stats_frame.pack(fill="x", padx=16, pady=(0, 16))
        
        # Create stat boxes
        self.stat_widgets = {}
        stat_items = [
            ("total", "Total Issues", "0", ModernTheme.COLORS['info']),
            ("critical", "Critical", "0", ModernTheme.COLORS['error']),
            ("errors", "Errors", "0", ModernTheme.COLORS['error']),
            ("warnings", "Warnings", "0", ModernTheme.COLORS['warning'])
        ]
        
        for i, (key, label, value, color) in enumerate(stat_items):
            stat_box = tk.Frame(
                stats_frame,
                bg=ModernTheme.COLORS['bg_tertiary'],
                relief="flat",
                bd=1,
                highlightbackground=color,
                highlightthickness=2
            )
            stat_box.pack(side="left", fill="x", expand=True, padx=(0, 8) if i < len(stat_items)-1 else (0, 0))
            
            value_label = tk.Label(
                stat_box,
                text=value,
                bg=ModernTheme.COLORS['bg_tertiary'],
                fg=color,
                font=('Segoe UI', 16, 'bold')
            )
            value_label.pack(pady=(8, 0))
            
            label_widget = tk.Label(
                stat_box,
                text=label,
                bg=ModernTheme.COLORS['bg_tertiary'],
                fg=ModernTheme.COLORS['text_secondary'],
                font=ModernTheme.FONTS['body']
            )
            label_widget.pack(pady=(0, 8))
            
            self.stat_widgets[key] = value_label
    
    def create_results_area(self, parent):
        """Create modern results area"""
        results_card = ModernCard(parent, title="📋 Analysis Results")
        results_card.pack(fill="both", expand=True)
        
        # Results text area with modern styling
        text_frame = tk.Frame(results_card, bg=ModernTheme.COLORS['bg_secondary'])
        text_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        
        self.result_text = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=ModernTheme.FONTS['mono'],
            bg=ModernTheme.COLORS['bg_primary'],
            fg=ModernTheme.COLORS['text_primary'],
            insertbackground=ModernTheme.COLORS['accent'],
            relief="flat",
            bd=0,
            padx=16,
            pady=16,
            selectbackground=ModernTheme.COLORS['accent'],
            selectforeground=ModernTheme.COLORS['text_primary']
        )
        self.result_text.pack(fill="both", expand=True)
        
        # Configure text tags for different levels
        for level, config in DETECTION_LEVELS.items():
            self.result_text.tag_config(
                level,
                foreground=config["color"],
                font=ModernTheme.FONTS['mono_bold']
            )
        
        self.result_text.tag_config(
            "HEADER",
            foreground=ModernTheme.COLORS['accent'],
            font=ModernTheme.FONTS['header']
        )
        
        self.result_text.tag_config(
            "LINE_NUMBER",
            foreground=ModernTheme.COLORS['text_muted'],
            font=ModernTheme.FONTS['mono']
        )
    
    def create_status_bar(self, parent):
        """Create modern status bar"""
        status_frame = tk.Frame(
            parent,
            bg=ModernTheme.COLORS['bg_secondary'],
            relief="flat",
            bd=1,
            highlightbackground=ModernTheme.COLORS['border'],
            highlightthickness=1
        )
        status_frame.pack(fill="x", pady=(16, 0))
        
        self.status_var = tk.StringVar(value="🚀 Ready to analyze your files!")
        self.status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            bg=ModernTheme.COLORS['bg_secondary'],
            fg=ModernTheme.COLORS['text_secondary'],
            font=ModernTheme.FONTS['body'],
            anchor="w"
        )
        self.status_label.pack(side="left", padx=16, pady=8)
        
        # Progress indicator (animated dots)
        self.progress_label = tk.Label(
            status_frame,
            text="",
            bg=ModernTheme.COLORS['bg_secondary'],
            fg=ModernTheme.COLORS['accent'],
            font=ModernTheme.FONTS['body']
        )
        self.progress_label.pack(side="right", padx=16, pady=8)
    
    def browse_file(self):
        """Modern file dialog"""
        filepath = filedialog.askopenfilename(
            title="🔍 Select File to Analyze",
            filetypes=[
                ("Log Files", "*.log"),
                ("Python Files", "*.py"),
                ("Text Files", "*.txt"),
                ("JavaScript Files", "*.js"),
                ("All Files", "*.*")
            ]
        )
        if filepath:
            self.file_var.set(filepath)
            self.current_file = filepath
            filename = os.path.basename(filepath)
            self.status_var.set(f"📁 Selected: {filename}")
            logging.info(f"File selected: {filepath}")
    
    def analyze_file(self):
        """Enhanced analysis with progress animation"""
        filepath = self.file_var.get()
        if not filepath or not os.path.exists(filepath):
            messagebox.showwarning("❌ Missing File", "Please select a valid file first.")
            return
        
        self.start_progress_animation()
        self.status_var.set("🔍 Analyzing file...")
        self.analyze_btn.label.config(text="Analyzing...")
        
        # Use after() to prevent UI blocking
        self.root.after(100, self.perform_analysis)
    
    def perform_analysis(self):
        """Perform the actual file analysis"""
        try:
            filepath = self.file_var.get()
            self.current_results = []
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    stripped_line = line.strip()
                    if not stripped_line:
                        continue
                    
                    detected_issues = self.detect_issues(stripped_line, line_num)
                    if detected_issues:
                        self.current_results.extend(detected_issues)
            
            self.stop_progress_animation()
            self.display_results()
            self.update_stats()
            self.analyze_btn.label.config(text="🔍 Analyze")
            
            total_issues = len(self.current_results)
            filename = os.path.basename(filepath)
            self.status_var.set(f"✅ Analysis complete! Found {total_issues} issues in {filename}")
            
            logging.info(f"Analysis completed: {total_issues} issues found in {filepath}")
        
        except Exception as e:
            self.stop_progress_animation()
            self.handle_error(f"Analysis error: {str(e)}")
            self.analyze_btn.label.config(text="🔍 Analyze")
    
    def detect_issues(self, line, line_num):
        return detect_rom_issues(line, line_num)
    
    def generate_message(self, level, line):
        """Generate contextual messages"""
        messages = {
            "CRITICAL": "System critical error detected",
            "ERROR": "Error condition found",
            "WARNING": "Potential issue identified", 
            "INFO": "Informational message",
            "CODE_SMELL": "Code quality issue",
            "PERFORMANCE": "Performance concern detected"
        }
        return messages.get(level, "Issue detected")
    
    def display_results(self):
        """Display results with modern formatting"""
        self.result_text.delete(1.0, tk.END)
        
        if not self.current_results:
            self.result_text.insert(tk.END, 
                "🎉 No issues found in the file!\n\n"
                "Your file appears to be clean and well-structured.", 
                "HEADER")
            return
        
        # Header
        filename = os.path.basename(self.current_file)
        self.result_text.insert(tk.END, 
            f"📊 Analysis Results for: {filename}\n"
            f"{'='*50}\n\n", 
            "HEADER")
        
        # Apply current filter
        self.filter_results()
    
    def filter_results(self):
        """Apply current filter to results"""
        if not self.current_results:
            return
            
        filter_level = self.filter_var.get()
        filtered_results = [
            r for r in self.current_results 
            if filter_level == "ALL" or r["level"] == filter_level
        ]
        
        # Clear results area but keep header
        content = self.result_text.get(1.0, tk.END)
        header_end = content.find('\n\n') + 2
        if header_end > 1:
            self.result_text.delete(f"1.{header_end}", tk.END)
        
        # Display filtered results
        for i, issue in enumerate(filtered_results, 1):
            # Issue header with icon and level
            self.result_text.insert(tk.END, 
                f"{issue['icon']} [{issue['level']}] ", 
                issue["level"])
            
            self.result_text.insert(tk.END, 
                f"Line {issue['line_num']}: {issue['message']}\n", 
                "LINE_NUMBER")
            
            # Code line with syntax highlighting
            self.result_text.insert(tk.END, 
                f"    {issue['line']}\n\n", 
                issue["level"])
        
        # Update filter status
        total = len(self.current_results)
        filtered = len(filtered_results)
        
        if filter_level != "ALL":
            self.status_var.set(f"📋 Showing {filtered} of {total} issues (filtered by {filter_level})")
        else:
            self.status_var.set(f"📋 Showing all {total} issues")
    
    def update_stats(self):
        """Update statistics display"""
        if not self.current_results:
            for widget in self.stat_widgets.values():
                widget.config(text="0")
            return
        
        # Count by level
        stats = {
            "total": len(self.current_results),
            "critical": len([r for r in self.current_results if r["level"] == "CRITICAL"]),
            "errors": len([r for r in self.current_results if r["level"] == "ERROR"]),
            "warnings": len([r for r in self.current_results if r["level"] == "WARNING"])
        }
        
        # Update widgets
        for key, count in stats.items():
            if key in self.stat_widgets:
                self.stat_widgets[key].config(text=str(count))
    
    def start_progress_animation(self):
        """Start animated progress indicator"""
        self.progress_dots = 0
        self.animate_progress()
    
    def animate_progress(self):
        """Animate progress dots"""
        dots = "." * (self.progress_dots % 4)
        self.progress_label.config(text=dots)
        self.progress_dots += 1
        self.animation_after_id = self.root.after(500, self.animate_progress)
    
    def stop_progress_animation(self):
        """Stop progress animation"""
        if self.animation_after_id:
            self.root.after_cancel(self.animation_after_id)
            self.animation_after_id = None
        self.progress_label.config(text="")
    
    def export_results(self):
        """Export results with modern formatting"""
        if not self.current_results:
            messagebox.showwarning("❌ No Results", "Nothing to export yet!")
            return
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.basename(self.current_file) if self.current_file else "unknown"
        
        export_text = f"""
🔍 Enhanced Log Seeker Analysis Report
=====================================
File: {self.current_file}
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Issues Found: {len(self.current_results)}

"""
        
        # Group by level
        by_level = {}
        for issue in self.current_results:
            level = issue["level"]
            if level not in by_level:
                by_level[level] = []
            by_level[level].append(issue)
        
        # Export by level
        for level in ["CRITICAL", "ERROR", "WARNING", "INFO", "CODE_SMELL", "PERFORMANCE"]:
            if level in by_level:
                issues = by_level[level]
                export_text += f"\n{DETECTION_LEVELS[level]['icon']} {level} ({len(issues)} issues)\n"
                export_text += "-" * 40 + "\n"
                
                for issue in issues:
                    export_text += f"Line {issue['line_num']}: {issue['message']}\n"
                    export_text += f"    {issue['line']}\n\n"
        
        # Copy to clipboard
        self.root.clipboard_clear()
        self.root.clipboard_append(export_text)
        
        # Save to file
        try:
            save_dir = os.path.dirname(self.current_file) if self.current_file else os.path.expanduser('~')
            save_path = os.path.join(save_dir, f"log_analysis_{filename}_{timestamp}.txt")
            
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(export_text)
                
            messagebox.showinfo(
                "✅ Export Complete", 
                f"Results exported successfully!\n\n"
                f"📋 Copied to clipboard\n"
                f"💾 Saved to: {save_path}"
            )
            
            logging.info(f"Results exported to {save_path}")
            
        except Exception as e:
            messagebox.showinfo(
                "⚠️ Partial Export", 
                f"Results copied to clipboard but couldn't save file:\n{str(e)}"
            )
    
    def handle_error(self, error_msg):
        """Enhanced error handling with modern UI"""
        self.stop_progress_animation()
        
        messagebox.showerror("💥 Error", error_msg)
        self.status_var.set(f"❌ {error_msg}")
        
        # Display error in results area
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, 
            "💥 Analysis Error\n"
            "================\n\n", "HEADER")
        self.result_text.insert(tk.END, 
            f"Error: {error_msg}\n\n"
            "Please check:\n"
            "• File exists and is readable\n"
            "• File is not corrupted\n"
            "• You have proper permissions\n", "ERROR")
        
        logging.error(f"Application error: {error_msg}")
    
    def create_context_menu(self):
        """Create modern context menu for results"""
        self.context_menu = tk.Menu(self.root, tearoff=0,
            bg=ModernTheme.COLORS['bg_secondary'],
            fg=ModernTheme.COLORS['text_primary'],
            activebackground=ModernTheme.COLORS['accent'],
            activeforeground=ModernTheme.COLORS['text_primary'],
            relief="flat",
            bd=1)
        
        self.context_menu.add_command(label="📋 Copy Line", command=self.copy_selected_line)
        self.context_menu.add_command(label="🔍 Search Similar", command=self.search_similar)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="📊 Show Statistics", command=self.show_detailed_stats)
        
        # Bind right-click to results text
        self.result_text.bind("<Button-3>", self.show_context_menu)
    
    def show_context_menu(self, event):
        """Show context menu"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def copy_selected_line(self):
        """Copy selected line to clipboard"""
        try:
            selection = self.result_text.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(selection)
            self.status_var.set("📋 Selected text copied to clipboard")
        except tk.TclError:
            self.status_var.set("⚠️ No text selected")
    
    def search_similar(self):
        """Search for similar issues"""
        try:
            selection = self.result_text.selection_get().strip()
            if selection:
                # Simple similarity search
                similar_count = sum(1 for issue in self.current_results 
                                  if selection.lower() in issue['line'].lower())
                self.status_var.set(f"🔍 Found {similar_count} similar issues")
        except tk.TclError:
            self.status_var.set("⚠️ No text selected for search")
    
    def show_detailed_stats(self):
        """Show detailed statistics in popup"""
        if not self.current_results:
            messagebox.showinfo("📊 Statistics", "No analysis results available")
            return
        
        # Calculate detailed stats
        stats_by_level = {}
        total_lines_analyzed = max(issue['line_num'] for issue in self.current_results) if self.current_results else 0
        
        for level in DETECTION_LEVELS.keys():
            count = len([r for r in self.current_results if r['level'] == level])
            if count > 0:
                stats_by_level[level] = count
        
        # Create stats message
        stats_msg = f"📊 Detailed Analysis Statistics\n"
        stats_msg += f"={'='*35}\n\n"
        stats_msg += f"📁 File: {os.path.basename(self.current_file)}\n"
        stats_msg += f"📏 Total Lines Scanned: {total_lines_analyzed}\n"
        stats_msg += f"🔍 Total Issues Found: {len(self.current_results)}\n\n"
        
        stats_msg += "Issue Breakdown:\n"
        for level, count in stats_by_level.items():
            icon = DETECTION_LEVELS[level]['icon']
            percentage = (count / len(self.current_results)) * 100
            stats_msg += f"{icon} {level}: {count} ({percentage:.1f}%)\n"
        
        if total_lines_analyzed > 0:
            issue_density = (len(self.current_results) / total_lines_analyzed) * 100
            stats_msg += f"\n📈 Issue Density: {issue_density:.2f}% of lines"
        
        messagebox.showinfo("📊 Detailed Statistics", stats_msg)
    
    def setup_keyboard_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.root.bind('<Control-o>', lambda e: self.browse_file())
        self.root.bind('<Control-r>', lambda e: self.analyze_file())
        self.root.bind('<Control-s>', lambda e: self.export_results())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.bind('<F5>', lambda e: self.analyze_file())
        
        # Add tooltip for shortcuts
        self.create_help_tooltip()
    
    def create_help_tooltip(self):
        """Create help tooltip with shortcuts"""
        help_text = """
🚀 Keyboard Shortcuts:
• Ctrl+O: Browse file
• Ctrl+R / F5: Analyze file  
• Ctrl+S: Export results
• Ctrl+Q: Quit application

💡 Pro Tips:
• Drag & drop files onto the window
• Use filters to focus on specific issue types
• Right-click in results for context menu
"""
        
        # Create help button
        self.help_btn = ModernButton(
            self.root,
            text="❓",
            command=lambda: messagebox.showinfo("🚀 Help & Shortcuts", help_text),
            style="secondary"
        )
        self.help_btn.place(relx=0.98, rely=0.02, anchor="ne")

def main():
    """Main application entry point"""
    root = tk.Tk()
    
    # Set window icon if available
    try:
        if os.path.exists('icon.ico'):
            root.iconbitmap('icon.ico')
    except:
        pass
    
    # Initialize app
    app = EnhancedLogSeeker(root)
    
    # Setup additional features
    app.create_context_menu()
    app.setup_keyboard_shortcuts()
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
