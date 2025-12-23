"""
Module για τη φόρτωση και την αρχική επικύρωση δεδομένων από Excel αρχεία
Windows Version
"""
import os
import re
import pandas as pd
from typing import Tuple
import xlrd
import openpyxl


# Import config με fallback
try:
    from . import config
except ImportError:
    import config


class DataLoader:
    """Κλάση για τη διαχείριση φόρτωσης δεδομένων"""
    

    def load_excel(self, file_path: str) -> pd.DataFrame:
        if not file_path or not os.path.exists(file_path):
            raise FileNotFoundError(f"Δεν βρέθηκε αρχείο: {file_path}")
        return pd.read_excel(file_path)


    def _list_available_files(self):
        """Εμφανίζει τα διαθέσιμα αρχεία στον BASE_PATH"""
        if os.path.exists(self.base_path):
            available_files = [
                f for f in os.listdir(self.base_path)
                if f.endswith(('.xls', '.xlsx'))
            ]
            if available_files:
                print("\n📁 Διαθέσιμα αρχεία στον φάκελο:")
                for f in sorted(available_files)[:10]:  # Εμφάνιση μέχρι 10 αρχείων
                    print(f"  - {f}")
                if len(available_files) > 10:
                    print(f"  ... και {len(available_files) - 10} ακόμα αρχεία")
            else:
                print("❌ Δεν βρέθηκαν αρχεία .xls ή .xlsx στον φάκελο.")
                print(f"   Τοποθετήστε τα αρχεία σας στο: {self.base_path}")
        else:
            print(f"❌ Ο φάκελος '{self.base_path}' δεν βρέθηκε.")
            print(f"   Δημιουργήστε τον φάκελο ή ελέγξτε το config.py")


def load_data() -> Tuple[pd.DataFrame, str, str]:
    """
    Wrapper function για εύκολη χρήση
    
    Returns:
        Tuple[DataFrame, str, str]: (excel_df, csv_first_4, dash_part)
    """
    loader = DataLoader()
    return loader.get_user_file()


if __name__ == "__main__":
    # Test του module
    print("=" * 70)
    print("TEST: Data Loader Module")
    print("=" * 70)
    
    excel_df, csv_first_4, dash_part = load_data()
    
    print(f"\n✅ Φορτώθηκαν {len(excel_df)} γραμμές")
    print(f"Στήλες: {excel_df.columns.tolist()}")
    print("\nΠρώτες 5 γραμμές:")
    print(excel_df.head())
