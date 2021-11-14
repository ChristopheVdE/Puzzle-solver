# Create board surface and fill it (background) ------------------------------------------------------------
    def BoardBackground(self, Background):
        self.BoardSurface = pygame.Surface((self.BoardSize, self.BoardSize), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.BoardSurface.fill(Background)