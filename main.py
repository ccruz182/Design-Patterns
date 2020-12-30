from buttons.checkbox_button import CheckboxButton
from buttons.dropdown_button import DropdownButton
from buttons.radio_button import RadioButton

from sizes.large_button import LargeButton
from sizes.medium_button import MediumButton
from sizes.small_button import SmallButton

large_check_button = CheckboxButton(LargeButton())
medium_dropdown_button = DropdownButton(MediumButton())
small_radio_button = RadioButton(SmallButton())

large_check_button.draw()
medium_dropdown_button.draw()
small_radio_button.draw()