import os

# Fungsi untuk menyimpan daftar tugas ke file
def save_tasks_to_file(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Fungsi untuk memuat daftar tugas dari file
def load_tasks_from_file(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Fungsi untuk menampilkan tugas menggunakan rekursi
def display_tasks(tasks, index=0):
    if index < len(tasks):
        print(f"{index + 1}. {tasks[index]}")
        display_tasks(tasks, index + 1)

# Fungsi untuk menambah tugas
def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

# Fungsi untuk mengedit tugas
def edit_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Pilih nomor tugas yang ingin diubah: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Masukkan deskripsi tugas baru: ")
        tasks[task_number] = new_task
        print("Tugas berhasil diperbarui!")
    else:
        print("Nomor tugas tidak valid!")

# Fungsi untuk menghapus tugas
def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Pilih nomor tugas yang ingin dihapus: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Tugas berhasil dihapus!")
    else:
        print("Nomor tugas tidak valid!")

# Fungsi utama program
def main():
    tasks = load_tasks_from_file()  # Memuat daftar tugas yang sudah disimpan sebelumnya
    while True:
        print("\n--- To-Do List ---")
        print("1. Tambah Tugas")
        print("2. Edit Tugas")
        print("3. Hapus Tugas")
        print("4. Tampilkan Tugas")
        print("5. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nDaftar Tugas:")
            display_tasks(tasks)  # Menampilkan tugas menggunakan rekursi
        elif choice == "5":
            save_tasks_to_file(tasks)  # Menyimpan tugas sebelum keluar
            print("Daftar tugas telah disimpan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
