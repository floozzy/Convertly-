from app.services.menu_service import build_main_menu, build_photo_menu


def test_main_menu_contains_expected_actions():
    menu = build_main_menu()
    labels = [button.text for row in menu.inline_keyboard for button in row]
    assert "🖼 Обработать фото" in labels
    assert "ℹ️ Помощь" in labels


def test_photo_menu_contains_operations():
    menu = build_photo_menu()
    labels = [button.text for row in menu.inline_keyboard for button in row]
    assert "⚫ Ч/Б" in labels
    assert "📏 Уменьшить" in labels
