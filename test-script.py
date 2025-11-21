"""
اسکریپت تست برای بررسی عملکرد Ollama و مدل‌ها
"""

import sys
import subprocess

def print_header(text):
    """چاپ هدر زیبا"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """بررسی نسخه Python"""
    print_header("🐍 بررسی نسخه Python")
    
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ نسخه Python مناسب است")
        return True
    else:
        print("❌ Python 3.8 یا بالاتر نیاز است")
        return False

def check_ollama_installed():
    """بررسی نصب Ollama"""
    print_header("🦙 بررسی نصب Ollama")
    
    try:
        result = subprocess.run(
            ['ollama', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print(f"✅ Ollama نصب شده است")
            print(f"   Version: {result.stdout.strip()}")
            return True
        else:
            print("❌ Ollama نصب نیست یا مشکل دارد")
            return False
            
    except FileNotFoundError:
        print("❌ Ollama یافت نشد")
        print("   لطفاً از https://ollama.com/download نصب کنید")
        return False
    except Exception as e:
        print(f"❌ خطا: {e}")
        return False

def check_ollama_running():
    """بررسی اجرای سرویس Ollama"""
    print_header("🔄 بررسی سرویس Ollama")
    
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("✅ سرویس Ollama در حال اجرا است")
            return True
        else:
            print("❌ سرویس Ollama در حال اجرا نیست")
            print("   لطفاً در ترمینال جدید اجرا کنید: ollama serve")
            return False
            
    except Exception as e:
        print(f"❌ خطا: {e}")
        print("   سرویس Ollama را با 'ollama serve' راه‌اندازی کنید")
        return False

def check_models():
    """بررسی مدل‌های نصب شده"""
    print_header("📦 بررسی مدل‌های نصب شده")
    
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            print("❌ نمی‌توان لیست مدل‌ها را دریافت کرد")
            return False
        
        output = result.stdout
        print("مدل‌های موجود:")
        print(output)
        
        required_models = ["gemma3:4b", "gemma3n:e4b"]
        found_models = []
        
        for model in required_models:
            if model in output:
                found_models.append(model)
                print(f"✅ {model} یافت شد")
            else:
                print(f"❌ {model} یافت نشد")
        
        if len(found_models) >= 2:
            print(f"\n✅ {len(found_models)} مدل آماده استفاده است")
            return True
        else:
            print("\n⚠️  حداقل دو مدل نیاز است")
            print("   برای دانلود مدل‌ها:")
            print("   ollama pull gemma3:4b")
            print("   ollama pull gemma3n:e4b")
            return False
            
    except Exception as e:
        print(f"❌ خطا: {e}")
        return False

def test_model_inference():
    """تست استنتاج مدل"""
    print_header("🧪 تست استنتاج مدل")
    
    try:
        import ollama
        
        print("در حال تست مدل gemma2:2b...")
        
        response = ollama.generate(
            model='gemma2:2b',
            prompt='سلام! یک جمله کوتاه فارسی بگو.',
            options={'num_predict': 50}
        )
        
        print(f"✅ مدل با موفقیت پاسخ داد:")
        print(f"   '{response['response'][:100]}...'")
        return True
        
    except ImportError:
        print("❌ کتابخانه ollama نصب نیست")
        print("   نصب کنید: pip install ollama")
        return False
    except Exception as e:
        print(f"❌ خطا در استنتاج: {e}")
        return False

def check_streamlit():
    """بررسی نصب Streamlit"""
    print_header("🎨 بررسی Streamlit")
    
    try:
        import streamlit
        print(f"✅ Streamlit نصب شده است (v{streamlit.__version__})")
        return True
    except ImportError:
        print("❌ Streamlit نصب نیست")
        print("   نصب کنید: pip install streamlit")
        return False

def check_disk_space():
    """بررسی فضای دیسک"""
    print_header("💾 بررسی فضای دیسک")
    
    try:
        import shutil
        
        total, used, free = shutil.disk_usage("/")
        
        free_gb = free // (2**30)
        print(f"فضای آزاد: {free_gb} GB")
        
        if free_gb > 5:
            print("✅ فضای دیسک کافی است")
            return True
        else:
            print("⚠️  فضای دیسک ممکن است کافی نباشد")
            return False
            
    except Exception as e:
        print(f"⚠️  نمی‌توان فضای دیسک را بررسی کرد: {e}")
        return True

def main():
    """اجرای تمام تست‌ها"""
    print("\n" + "🔍 شروع بررسی سیستم...")
    
    checks = {
        "Python Version": check_python_version(),
        "Ollama Installed": check_ollama_installed(),
        "Ollama Running": check_ollama_running(),
        "Models": check_models(),
        "Streamlit": check_streamlit(),
        "Disk Space": check_disk_space(),
    }
    
    # امتحان کردن inference (فقط اگه بقیه OK باشند)
    if all([checks["Ollama Installed"], checks["Ollama Running"], checks["Models"]]):
        checks["Model Inference"] = test_model_inference()
    
    # خلاصه نتایج
    print_header("📊 خلاصه نتایج")
    
    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
    
    print("\n" + "="*60)
    
    if all(checks.values()):
        print("\n🎉 تمام تست‌ها موفق بود! شما آماده اجرای برنامه هستید.")
        print("   برای اجرا: streamlit run app.py")
    else:
        print("\n⚠️  برخی مشکلات وجود دارد. لطفاً آنها را برطرف کنید.")
        print("\nراهنمای رفع مشکلات:")
        
        if not checks.get("Ollama Installed", True):
            print("  1. Ollama را از https://ollama.com/download نصب کنید")
        
        if not checks.get("Ollama Running", True):
            print("  2. Ollama را اجرا کنید: ollama serve")
        
        if not checks.get("Models", True):
            print("  3. مدل‌ها را دانلود کنید:")
            print("     ollama pull gemma3:4b")
            print("     ollama pull gemma3n:e4b")
        
        if not checks.get("Streamlit", True):
            print("  4. Streamlit را نصب کنید:")
            print("     pip install streamlit ollama")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()