import os
from dotenv import load_dotenv

load_dotenv()

env_vars = [
    "GMAIL",
    "OUTLOOK",
    "M2U_FPX_ID",
    "M2U_FXP_PASSWORD",
    "M2U_MASTERCARD_ID",
    "M2U_VISA_ID",
    "M2U_CC_ID",
    "M2U_CC_CSV",
    "M2U_CSV",
    "M2U_EXPIRY_DATE",
    "M2U_MERCHANT_ID",
    "M2U_OTP_URL"
]

def test_env_variables_loaded():
    all_passed = True
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: PASSED")
        else:
            print(f"❌ {var}: FAILED")
            all_passed = False
    assert all_passed, "Some environment variables are missing!"
