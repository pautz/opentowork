import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import Qt, QUrl

class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, nav_type, isMainFrame):
        url_str = url.toString()
        # Intercepta qualquer tentativa de ir para locason.php (mesmo com parâmetros)
        if "locason.php" in url_str:
            self.view().setUrl(QUrl("https://carlitoslocacoes.com/site/reserva_pendente_barcos.php"))
            return False  # Cancela o carregamento original
        return super().acceptNavigationRequest(url, nav_type, isMainFrame)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reserva de Barcos")
        self.setGeometry(100, 100, 1200, 800)

        # Mantém a janela sempre no topo
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Cria um perfil persistente para guardar cookies/localStorage
        profile = QWebEngineProfile("MeuPerfil", self)
        profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)

        # Usa a página customizada
        page = CustomWebEnginePage(profile, self)

        # Cria o navegador e associa a página
        self.browser = QWebEngineView()
        self.browser.setPage(page)
        self.browser.load(QUrl("https://carlitoslocacoes.com/site/reserva_pendente_barcos.php"))

        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
