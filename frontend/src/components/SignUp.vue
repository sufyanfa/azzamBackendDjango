<template>
    <div class="form">
        <form action="./login.html" class="form__content">
          <h1 class="text-lg font-bold">نظام إدارة المدعوين</h1>
            <div class="form__box">
                <input required type="email" class="form__input focus:outline-none focus:border-black focus:ring-black" placeholder="البريد">
                <label for="" class="form__label">ادخل البريد</label>
                <div class="form__shadow"></div>
            </div>

            <div class="form__box">
                <input required type="password" class="form__input focus:outline-none focus:border-black focus:ring-black" placeholder="كلمة المرور">
                <label for="" class="form__label">ادخل كلمة المرور</label>
                <div class="form__shadow"></div>
            </div>
  
            <div class="form__button">
                <input type="Submit" class="form__submit" value="دخول">
            </div>
        </form>
    </div>
</template>