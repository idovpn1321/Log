#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import os
import re
import subprocess
from datetime import datetime

class MaterialYouTheme:
    @staticmethod
    def get_gnome_color_scheme():
        """Detect GNOME dark/light mode"""
        try:
            result = subprocess.run(
                ['gsettings', 'get', 'org.gnome.desktop.interface', 'color-scheme'],
                capture_output=True, text=True
            )
            if 'dark' in result.stdout.lower():
                return 'dark'
        except:
            pass
        return 'light'

    @staticmethod
    def get_theme(theme_mode):
        """Material You colors matching GNOME's Adwaita palette"""
        return {
            'dark': {
                'primary': '#3584e4',  # GNOME blue
                'surface': '#242424',
                'background': '#1e1e1e',
                'error': '#ff7b63',
                'warning': '#ffbe6f',
                'info': '#41a6b5',
                'success': '#8ff0a4',
                'text': '#ffffff',
                'secondary': '#deddda'
            },
            'light': {
                'primary': '#1a5fb4',  # GNOME blue
                'surface': '#ffffff',
                'background': '#f6f5f4',
                'error': '#c01c28',
                'warning': '#e5a50a',
                'info': '#1a5fb4',
                'success': '#26a269',
                'text': '#241f31',
                'secondary': '#5e5c64'
            }
        }[theme_mode]

class LinuxLogSeeker:
    def __init__(self, root):
        self.root = root
        self.theme = MaterialYouTheme.get_theme(
            MaterialYouTheme.get_gnome_color_scheme()
        )
        self.setup_ui()
        self.setup_logging()
        self.current_file = ""
        self.current_results = []
        
        # Linux-specific initialization
        self.setup_linux_environment()

    def setup_linux_environment(self):
        """Linux-specific setup"""
        # Set WM_CLASS for proper window management
        self.root.wm_class("ZuanLogSeekr")
        
        # Use CSD if available
        try:
            self.root.attributes('-type', 'dialog')
        except:
            pass

    def setup_logging(self):
        """Linux-appropriate logging"""
        log_dir = os.path.expanduser("~/.local/share/zuanlogseeker")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            filename=os.path.join(log_dir, 'app.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Linux Log Seeker started")

    def setup_ui(self):
        """GTK-inspired Material You interface"""
        self.root.title("ZuanLogSeekr for Linux")
        self.root.geometry("1000x700")
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=12)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header bar inspired by GNOME
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 12))
        
        ttk.Label(
            header_frame,
            text="ZuanLogSeekr",
            font=('Cantarell 11 bold'),
            foreground=self.theme['primary']
        ).pack(side=tk.LEFT)
        
        # Theme toggle button
        self.theme_btn = ttk.Button(
            header_frame,
            text="🌓",
            command=self.toggle_theme,
            width=3
        )
        self.theme_btn.pack(side=tk.RIGHT, padx=4)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 12))
        
        # File selection
        file_btn = ttk.Button(
            control_frame,
            text="Open File",
            command=self.browse_file,
            style='primary.TButton'
        )
        file_btn.pack(side=tk.LEFT, padx=4)
        
        self.file_label = ttk.Label(
            control_frame,
            text="No file selected",
            foreground=self.theme['secondary']
        )
        self.file_label.pack(side=tk.LEFT, padx=8)
        
        # Analysis button
        analyze_btn = ttk.Button(
            control_frame,
            text="Analyze",
            command=self.analyze_file,
            style='primary.TButton'
        )
        analyze_btn.pack(side=tk.RIGHT, padx=4)
        
        # Results area
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=('Cantarell 10'),
            height=25,
            padx=12,
            pady=12,
            bg=self.theme['surface'],
            fg=self.theme['text'],
            insertbackground=self.theme['text'],
            selectbackground=self.theme['primary'],
            relief=tk.FLAT
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags
        tags_config = {
            'ERROR': {'foreground': self.theme['error'], 'font': 'Cantarell 10 bold'},
            'WARNING': {'foreground': self.theme['warning'], 'font': 'Cantarell 10 bold'},
            'INFO': {'foreground': self.theme['info'], 'font': 'Cantarell 10'},
            'SUCCESS': {'foreground': self.theme['success'], 'font': 'Cantarell 10 bold'},
            'HEADER': {'foreground': self.theme['primary'], 'font': 'Cantarell 12 bold'}
        }
        
        for tag, config in tags_config.items():
            self.result_text.tag_config(tag, **config)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to analyze files")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.FLAT,
            anchor=tk.W,
            font=('Cantarell 9'),
            foreground=self.theme['secondary']
        )
        status_bar.pack(fill=tk.X, pady=(6, 0))
        
        # Apply theme colors
        self.apply_theme_colors()

    def apply_theme_colors(self):
        """Apply Material You colors to all widgets"""
        style = ttk.Style()
        
        # Configure styles
        style.configure(
            '.',
            background=self.theme['background'],
            foreground=self.theme['text'],
            font=('Cantarell 10')
        )
        
        style.configure(
            'TFrame',
            background=self.theme['background']
        )
        
        style.configure(
            'TButton',
            background=self.theme['primary'],
            foreground='white',
            bordercolor=self.theme['primary'],
            focuscolor=self.theme['primary'] + '30',
            padding=6
        )
        
        style.map(
            'TButton',
            background=[('active', self.theme['primary'] + 'CC')],
            bordercolor=[('active', self.theme['primary'] + 'CC')]
        )
        
        # Configure entry widget
        style.configure(
            'TEntry',
            fieldbackground=self.theme['surface'],
            foreground=self.theme['text'],
            insertcolor=self.theme['text'],
            bordercolor=self.theme['secondary'],
            lightcolor=self.theme['secondary'],
            darkcolor=self.theme['secondary']
        )

    def toggle_theme(self):
        """Switch between dark/light mode"""
        current_theme = MaterialYouTheme.get_gnome_color_scheme()
        new_theme = 'light' if current_theme == 'dark' else 'dark'
        self.theme = MaterialYouTheme.get_theme(new_theme)
        self.apply_theme_colors()
        
        # Update text widget colors
        self.result_text.configure(
            bg=self.theme['surface'],
            fg=self.theme['text'],
            insertbackground=self.theme['text']
        )
        
        # Re-apply text tags with new colors
        tags_config = {
            'ERROR': {'foreground': self.theme['error']},
            'WARNING': {'foreground': self.theme['warning']},
            'INFO': {'foreground': self.theme['info']},
            'SUCCESS': {'foreground': self.theme['success']},
            'HEADER': {'foreground': self.theme['primary']}
        }
        
        for tag, config in tags_config.items():
            self.result_text.tag_config(tag, **config)
        
        self.status_var.set(f"Switched to {new_theme} mode")

    # ... [Keep all other methods from previous version] ...

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set GNOME-friendly window attributes
    try:
        root.attributes('-zoomed', False)  # Don't start maximized
        root.attributes('-type', 'normal')
    except:
        pass
    
    app = LinuxLogSeeker(root)
    root.mainloop()
