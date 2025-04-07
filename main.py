from principal.main_app import view_main
from principal.main_components import create_main_app, create_custom_buttom, close_view, create_image, create_view

main_app = create_main_app()
view_main(main_app)
main_app.mainloop()
