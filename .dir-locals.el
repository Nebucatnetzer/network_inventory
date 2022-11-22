;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((eval progn
       (setenv "DJANGO_SETTINGS_MODULE" "network_inventory.settings.local")
       (setenv "PYTEST_ADDOPTS" "-n 4 --nomigrations"))))
