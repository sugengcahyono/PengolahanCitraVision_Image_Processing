# def open_image_and_apply_histogram_equalization_triggered(self):
#         """
#         Menerapkan Fuzzy Histogram Equalization pada gambar yang telah dibuka.
#         """
#         if self.original_image is None:
#             QMessageBox.warning(self, "Warning", "Tidak ada gambar yang dibuka. Silakan buka gambar terlebih dahulu.")
#             return
        
#         try:
#             # Konversi gambar dari PIL Image ke NumPy array (RGB format)
#             original_image_np = np.array(self.original_image.convert('RGB'))
            
#             # Menerapkan fuzzy histogram equalization pada gambar RGB
#             equalized_image_np = fuzzy_histogram_equalization(original_image_np)
            
#             # Konversi kembali hasil dari NumPy ke PIL Image untuk penyimpanan
#             equalized_image_pil = Image.fromarray(equalized_image_np)
            
#             # Tampilkan hasilnya di QLabel processedImageLabel
#             display_image(equalized_image_pil, self.processedImageLabel)
            
#             # Simpan gambar yang telah diproses untuk digunakan oleh fungsi save_image
#             self.processed_image = equalized_image_pil
        
#         except Exception as e:
#             QMessageBox.critical(self, "Error", f"Failed to apply histogram equalization: {str(e)}")

#     def open_image_and_apply_fuzzy_rgb(self):
#         """
#         Menerapkan Fuzzy Histogram Equalization pada gambar RGB yang telah dibuka.
#         """
#         if self.original_image is None:
#             QMessageBox.warning(self, "Warning", "Tidak ada gambar yang dibuka. Silakan buka gambar terlebih dahulu.")
#             return

#         try:
#             # Mengonversi gambar PIL ke format numpy array (RGB)
#             original_image_rgb = np.array(self.original_image)

#             # Memastikan gambar memiliki 3 channel (RGB)
#             if original_image_rgb is None or len(original_image_rgb.shape) != 3 or original_image_rgb.shape[2] != 3:
#                 raise ValueError("Gambar bukan gambar RGB.")

#             # Menampilkan gambar asli di QLabel pertama (originalImageLabel)
#             display_image(original_image_rgb, self.originalImageLabel)

#             # Menerapkan fuzzy histogram equalization pada gambar RGB
#             fuzzy_histogram_equalization_rgb(self)  # Mengirimkan instance dari self

#             # Simpan gambar yang diproses untuk keperluan save
#             self.processed_image = Image.fromarray(original_image_rgb)

#         except ValueError as e:
#             # Menampilkan pesan kesalahan jika terjadi error
#             QMessageBox.critical(self, "Error", str(e))