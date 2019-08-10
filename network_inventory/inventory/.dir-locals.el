;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode
  (pyvenv-activate . "~/git_repos/projects/network_inventory/venv/")
  (eval progn
        (setenv "DJANGO_SETTINGS_MODULE" "network_inventory.settings.local")))
