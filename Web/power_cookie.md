![chal](https://github.com/user-attachments/assets/54836bc0-6567-447c-a42c-08e8128aa5bc)


Using `BurpSuite` to access to the web page, I see that there's a `isAdmin` field in the HTTP request and it's set to `0`, keep that value and we see that we can't access to the web page.

![isAdmin0](https://github.com/user-attachments/assets/73660846-228d-43d4-a74f-9fd307f45c81)


![failed](https://github.com/user-attachments/assets/ffb86f3d-146e-4626-8fad-278e7b27510f)


But if we change to `1`, then we successfully get into the web page and get the flag.

![flag](https://github.com/user-attachments/assets/968315e8-d241-4e7d-b2d0-335e019a7cba)
