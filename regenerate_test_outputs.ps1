
python.exe .\mac2winKeyboard.py .\tests\dummy.keylayout `
  --physical_layout us `
  --language_id 409 --language_tag en-US --language_name "English (United States)" `
  --keyboard_description "Dummy - Mac" `
  --company_name "myCompany"

python.exe .\mac2winKeyboard.py .\tests\french.keylayout `
  --physical_layout international `
  --language_id 40c --language_tag fr-FR --language_name "French (France)" `
  --keyboard_description "French - Mac" `
  --company_name "myCompany"

python.exe .\mac2winKeyboard.py .\tests\german.keylayout `
  --physical_layout international `
  --language_id 407 --language_tag de-DE --language_name "German (Germany)" `
  --keyboard_description "German - Mac" `
  --company_name "myCompany"

python.exe .\mac2winKeyboard.py .\tests\sgcap.keylayout `
  --physical_layout us `
  --language_id 409 --language_tag en-US --language_name "English (United States)" `
  --keyboard_description "SGCAP example - Mac" `
  --company_name "myCompany"

python.exe .\mac2winKeyboard.py .\tests\us_test.keylayout `
  --physical_layout us `
  --language_id 409 --language_tag en-US --language_name "English (United States)" `
  --keyboard_description "US - Mac" `
  --company_name "myCompany"

# TODO do this automatically
echo 'Please replace the current year with $YEAR manually in the files!'
